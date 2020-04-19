from konlpy.tag import Okt
okt = Okt()
malist = okt.pos("아버지 가방에 들어가신다.", norm=True, stem=True) # norm은 문장을 정규화. stem은 각 단어에서 어간을 추출.(기본값은 둘다 False)
print(malist)

malist = okt.pos("그래욬ㅋㅋ! 아버지 가방에 10시에 들어가셨다.", norm=True, stem=True) # norm은 문장을 정규화. stem은 각 단어에서 어간을 추출.(기본값은 둘다 False)
print(malist)