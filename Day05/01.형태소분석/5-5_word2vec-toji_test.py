from gensim.models import word2vec
from pprint import pprint

# 모델 출력하기
model = word2vec.Word2Vec.load("./file/toji.model")
a = model.most_similar(positive=["땅"]) # 가까운 단어
b = model.most_similar(negative=["땅"])  # 먼 단어
pprint(a)
pprint(b)