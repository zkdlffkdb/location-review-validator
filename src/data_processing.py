#%% imports
import pandas as pd
from datetime import datetime
import os
import numpy as np
from textblob import TextBlob
from scipy.stats import spearmanr, pearsonr, chi2_contingency

#%% Helper functions
def add_text_features(df, text_col="review_text"):
    df = df.copy()
    df["text_length_words"] = df[text_col].fillna("").apply(lambda x: len(x.split()))
    df["sentiment_polarity"] = df[text_col].fillna("").apply(lambda x: TextBlob(x).sentiment.polarity)
    df["sentiment_subjectivity"] = df[text_col].fillna("").apply(lambda x: TextBlob(x).sentiment.subjectivity)
    return df


#%%
data_folder = 'data'
reviews_df = pd.read_csv(f'{data_folder}/restaurants-and-shops-detailed-reviews.csv')
overview_df = pd.read_csv(f'{data_folder}/restaurants-and-shops-overview.csv')

#%%
# data cleaning - unlabelled data
merged_df = pd.merge(reviews_df,
                     overview_df,
                     on='place_id',
                     how='left', 
                     suffixes=('_person', '_place')) # rename columns with same name: name (person's name and place name)

output_raw_file = f'{data_folder}/unlabelled_raw_data.csv'
merged_df.to_csv(output_raw_file, index=False)
print('unlabelled_raw_data.csv has been outputted in data folder')
# print('Details of raw data:')
# print(merged_df.describe())



#%%
# if review_translated_text is not empty, replace review_text with this
review_replace_mask = merged_df['review_translated_text'].notna()
merged_df.loc[review_replace_mask, 'review_text'] = merged_df.loc[review_replace_mask, 'review_translated_text']

# if response_from_owner_translated_text is not empty, replace response_from_owner_text with this
response_replace_mask = merged_df['response_from_owner_translated_text'].notna()
merged_df.loc[response_replace_mask, 'response_from_owner_text'] = merged_df.loc[response_replace_mask, 'response_from_owner_translated_text']

# place_name from reviews_df can be dropped as it is the same as name_place from overview_df
# name, name_person and owner_name can be dropped as they don't provide any insight for analysis
# query, review_translated_text and response_from_owner_translated_text can also be dropped
# links and image links can be dropped as they don't provide any insight for analysis
# is_temporarily_closed is dropped as it is an empty column
# Since place_id and review_id and reviewer_id are high-cardinality columns that 
# are not useful as features, they should be removed
# see eda.ipynb for more details
drop_cols = ['place_name', 'name_person', 'owner_name', 'query', 'review_translated_text', 
             'response_from_owner_translated_text', 'review_link', 'phone', 'link', 'website',
             'reviewer_profile', 'owner_profile_link', 'featured_image', 'review_photos',
             'link', 'is_temporarily_closed', 'place_id', 'review_id', 'reviewer_id']
merged_df.drop(columns=[c for c in drop_cols if c in merged_df.columns], inplace=True, errors="ignore")

# data scraped on 26/7/2025
# calculate no. of days since review was submitted to make published_at more useful
# convert published_at value to be no. of days since review was submitted
# rename published_at to published_ago to explain the column better
merged_df['published_at_date'] = pd.to_datetime(merged_df['published_at_date'])
merged_df['published_at'] = (datetime(2025, 8, 26) - merged_df['published_at_date']).dt.days
merged_df = merged_df.rename(columns={'published_at': 'published_ago'})

# calculate no. of days since owner responded to make response_from_owner_date more useful
# convert response_from_owner_ago value to be no. of days since owner responded
merged_df['response_from_owner_date'] = pd.to_datetime(merged_df['response_from_owner_date'], errors='coerce')
merged_df['response_from_owner_ago'] = merged_df['response_from_owner_date'].apply(lambda x: (datetime(2025, 8, 26) - x).days if not pd.isnull(x) else None)
merged_df.drop(columns=['published_at_date', 'response_from_owner_date'], inplace=True)

# convert NaN to 0 for is_local_guide, is_spending_on_ads, can_claim
bool_cols = ["is_local_guide", "is_spending_on_ads", "can_claim"]
for col in bool_cols:
    if col in merged_df.columns:
        merged_df[col] = merged_df[col].fillna(0).astype(int)

tentative_drop_cols = ['name_place', 'response_from_owner_text', 'experience_details', 'description', 'competitors', 'workday_timing', 'closed_on',
                       'address', 'review_keywords', 'published_ago', 'response_from_owner_ago', 'categories']
merged_df.drop(columns=[c for c in tentative_drop_cols if c in merged_df.columns], inplace=True, errors="ignore")

#%%
df_feat = add_text_features(merged_df, text_col="review_text")

numeric_cols = [
    'rating_person', 'rating_place', 
    'total_number_of_reviews_by_reviewer', 
    'total_number_of_photos_by_reviewer', 
    'reviews'
]

categorical_cols = [
    'main_category', 'is_local_guide', 
    'is_spending_on_ads', 'can_claim'
]

text_features = ["text_length_words","sentiment_polarity","sentiment_subjectivity"]

#%%
output_file = f'{data_folder}/cleaned_data.csv'
df_feat.to_csv(output_file, index=False)
print('cleaned_data.csv has been outputted in data folder')