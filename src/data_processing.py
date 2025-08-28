#%% imports
import pandas as pd
from datetime import datetime
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

print('Details of raw data:')
print(merged_df.describe())

#%%
# if review_translated_text is not empty, replace review_text with this
review_replace_mask = merged_df['review_translated_text'].notna()
merged_df.loc[review_replace_mask, 'review_text'] = merged_df.loc[review_replace_mask, 'review_translated_text']

# if response_from_owner_translated_text is not empty, replace response_from_owner_text with this
response_replace_mask = merged_df['response_from_owner_translated_text'].notna()
merged_df.loc[response_replace_mask, 'response_from_owner_text'] = merged_df.loc[response_replace_mask, 'response_from_owner_translated_text']

# place_name from reviews_df can be dropped as it is the same as name from overview_df
# query, review_translated_text and response_from_owner_translated_text can also be dropped
# links can be dropped as they don't provide any insight for analysis
# is_temporarily_closed is dropped as it is an empty column
merged_df.drop(columns=['place_name', 'query', 'review_translated_text', 
                        'response_from_owner_translated_text', 'review_link',
                        'reviewer_profile', 'owner_profile_link', 'featured_image',
                        'link', 'is_temporarily_closed'], inplace=True)

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

#%%
output_file = f'{data_folder}/unlabelled_data.csv'
merged_df.to_csv(output_file, index=False)
print('unlabelled_data.csv has been outputted in data folder')
