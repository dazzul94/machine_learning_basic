##-----------------------------------------------------
# Scikit-Learn 
# 패키지는 분류(classification) 모형의 테스트를 위해 
# 여러가지 가상 데이터를 생성하는 함수를 제공한다.
##-----------------------------------------------------
##
## make_gaussian_quantiles
from matplotlib import pyplot as plt
from sklearn.datasets import make_gaussian_quantiles

plt.title("등고선으로 구분되는 두 개의 클러스터를 가진 가상 데이터")
X, y = make_gaussian_quantiles(n_samples=400, n_features=2, n_classes=2, random_state=0)
plt.scatter(X[:, 0], X[:, 1], marker='o', c=y, s=100,
            edgecolor="k", linewidth=2)
plt.xlabel("$X_1$")
plt.ylabel("$X_2$")
plt.show()