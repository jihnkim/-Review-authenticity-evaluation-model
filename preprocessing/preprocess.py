import pandas as pd
from google_review_preprocessing import *
from tqdm import tqdm

df = pd.read_csv('google_review.csv')
# df = df.iloc[0:30, :]

pre_df = df['review']

review_row = pre_df.to_list()
review_row = clean_text(review_row)

preprocessed_review_row = []
for idx, review in tqdm(enumerate(review_row)):
    try:
        review = spell_check(review)
        review = kospacing(review)
        review = repeat_limitation(review)
        review = clean_punc(review)

        preprocessed_review_row.append(review)

    except Exception as e1:
        print(e1)
        preprocessed_review_row.append('')
        continue


# print(preprocessed_review_row)
# print(len(preprocessed_review_row))

df['preprocessed_review'] = preprocessed_review_row
# df = df.drop(columns=['Unnamed: 0'], axis=1)

df.to_csv('google_review_preprocessed.csv', index=False)

