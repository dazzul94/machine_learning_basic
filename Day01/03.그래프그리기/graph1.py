import numpy as np
import matplotlib.pyplot as plt

# data 작성
np.random.seed(1) # random number
x = np.arange(10)
y = np.random.rand(10)

# 그래프 표시
plt.plot(x, y) # 꺾은선 그래프를 
plt.show() # 그래프 그리기