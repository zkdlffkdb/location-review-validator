#%% imports
import pandas as pd

#%%
data_folder = 'data'
reviews_df = pd.read_csv(f'{data_folder}/restaurants-and-shops-detailed-reviews.csv')
overview_df = pd.read_csv(f'{data_folder}/restaurants-and-shops-overview.csv')

#%%
merged_df = pd.merge(reviews_df,
                     overview_df,
                     on='place_id',
                     how='left', 
                     suffixes=('_person', '_place')) # rename columns with same name: name (person's name and place name)

# if review_translated_text is not empty, replace review_text with this
review_replace_mask = merged_df['review_translated_text'].notna()
merged_df.loc[review_replace_mask, 'review_text'] = merged_df.loc[review_replace_mask, 'review_translated_text']

# if response_from_owner_translated_text is not empty, replace response_from_owner_text with this
response_replace_mask = merged_df['response_from_owner_translated_text'].notna()
merged_df.loc[response_replace_mask, 'response_from_owner_text'] = merged_df.loc[response_replace_mask, 'response_from_owner_translated_text']

# place_name from reviews_df can be dropped as it is the same as name from overview_df
# query, review_translated_text and response_from_owner_translated_text can also be dropped
merged_df.drop(columns=['place_name', 'query', 'review_translated_text', 'response_from_owner_translated_text'], inplace=True)
#%%
output_file = f'{data_folder}/unlabelled_data.csv'
merged_df.to_csv(output_file, index=False)
print('unlabelled_data.csv has been outputted in data folder')
