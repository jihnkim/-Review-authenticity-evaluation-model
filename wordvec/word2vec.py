from konlpy.tag import Okt
from konlpy.tag import Mecab
import pandas as pd
from tqdm import tqdm

df = pd.read_csv('google_review_preprocessed.csv')
pre_df = df['preprocessed_review']
pre_df = pre_df.dropna()
pre_df = pre_df[:100]

token = Okt()
tokenized_lst = []
for lines in tqdm(pre_df):
    review = token.morphs(lines)
    tokenized_lst.append(review)
    # print(review)

print(tokenized_lst)

# word2vec

from gensim.models import word2vec
from konlpy.utils import pprint

model = word2vec.Word2Vec(tokenized_lst, vector_size=100, window=10, hs=1, min_count=2, sg=1)
model.save('practice.model')
print('ok')

model = word2vec.Word2Vec.load('practice.model')

