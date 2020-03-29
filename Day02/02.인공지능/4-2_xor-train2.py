import pandas as pd # 행렬에 특화되어 있는 라이브러리
from sklearn import svm, metrics
# XOR 연산
xor_input = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
# 입력을 학습 전용 데이터와 테스트 전용 데이터로 분류하기 --- (※1)
xor_df = pd.DataFrame(xor_input)
print(xor_df)
# exit()

# 행렬을 만들어서 반복문을 돌아서 넣었었는데 판다스를 이용하면 쉽게 데이터와 레이블을 구분할 수 있다.
# df.loc[행 인덱싱값, 열 인덱싱값]
xor_data  = xor_df.loc[:,0:1] # 데이터
xor_label = xor_df.loc[:,2]   # 레이블
# 데이터 학습과 예측하기 --- (※2)
clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)
# 정답률 구하기 --- (※3)
# xor_label: real data
# pre : predicted data
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률 =", ac_score)