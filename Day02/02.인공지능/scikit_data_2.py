##-----------------------------------------------------
# Scikit-Learn 
# 패키지는 분류(classification) 모형의 테스트를 위해 
# 여러가지 가상 데이터를 생성하는 함수를 제공한다.
##-----------------------------------------------------
##
# make_classification
from matplotlib import pyplot as plt
from sklearn.datasets import make_classification

plt.title("1개의 독립변수를 가진 가상 데이터")
X, y = make_classification(n_features=1, n_informative=1,
                           n_redundant=0, n_clusters_per_class=1, random_state=4)
plt.scatter(X, y, marker='o', c=y,
            s=100, edgecolor="k", linewidth=2)

plt.xlabel("$X$")
plt.ylabel("$y$")
plt.show()