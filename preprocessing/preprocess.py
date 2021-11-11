import pandas as pd
from google_review_preprocessing import *
from tqdm import tqdm

df = pd.read_csv('google_review_1_10.csv')

df = df.iloc[0:500, :]

pre_df = df['review']

review_row = pre_df.to_list()
review_row = clean_text(review_row)

preprocessed_review_row = []
for idx, review in tqdm(enumerate(review_row)):
    review = spell_check(review)
    review = kospacing(review)
    review = repeat_limitation(review)
    review = clean_punc(review)

    preprocessed_review_row. append(review)

print(preprocessed_review_row)
print(len(preprocessed_review_row))

