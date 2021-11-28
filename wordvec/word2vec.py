from konlpy.tag import Okt
from konlpy.tag import Mecab
import pandas as pd
from gensim.models import word2vec
from tqdm import tqdm
# plt 한글 깨짐 처리
import matplotlib.pyplot as plt
import platform

if platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic')
elif platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic')

plt.rcParams['axes.unicode_minus'] = False


df = pd.read_csv('google_review_final.csv')


# # 데이터 전처리 추가
# df['preprocessed_review'] = df['preprocessed_review'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "")
# df.to_csv('google_review_final.csv', index=False)

pre_df = df
pre_df = pre_df[:100]
pre_df.dropna()

# define stopwords
stopwords = ['의','가','이','은','들','는','좀','잘','걍','과','도','를','으로','자','에','와','한','하다']

# split with okt
token = Okt()
tokenized_lst = []
for lines in tqdm(pre_df['preprocessed_review'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]", "")):
    review = token.morphs(lines)
    review = [word for word in review if not word in stopwords]
    tokenized_lst.append(review)

print(tokenized_lst)


# word2vec
model = word2vec.Word2Vec(tokenized_lst,
                          vector_size=100,
                          window=4,
                          hs=1,
                          min_count=2,
                          sg=1)

model.save('practice.model')
print('ok')

model = word2vec.Word2Vec.load('practice.model')

temp = model.wv.index_to_key
print(temp)


# # 시각화
#
# word_vectors = model.wv
# vocabs = word_vectors.index_to_key
# word_vectors_list = [word_vectors[v] for v in vocabs]
#
# from sklearn.manifold import TSNE
# from sklearn.decomposition import PCA
# from gensim.models import KeyedVectors
#
# from sklearn.decomposition import PCA
# pca = PCA(n_components=2)
# xys = pca.fit_transform(word_vectors_list)
# xs = xys[:,0]
# ys = xys[:,1]
#
# def plot_2d_graph(vocabs, xs, ys):
#     plt.figure(figsize=(15, 10))
#     plt.scatter(xs, ys, marker='o')
#     for i, v in enumerate(vocabs):
#         plt.annotate(v, xy=(xs[i], ys[i]))
#
# plot_2d_graph(vocabs, xs, ys)
# plt.show()
