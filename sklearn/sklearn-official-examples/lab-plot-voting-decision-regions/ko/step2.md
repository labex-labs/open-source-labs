# 분류기 학습

`DecisionTreeClassifier`, `KNeighborsClassifier`, 그리고 `SVC` 세 가지 분류기를 초기화합니다. 그런 다음 이 세 가지 분류기를 사용하여 `VotingClassifier`를 초기화하고, 이를 사용하여 아이리스 꽃의 종류를 예측합니다.

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier

clf1 = DecisionTreeClassifier(max_depth=4)
clf2 = KNeighborsClassifier(n_neighbors=7)
clf3 = SVC(gamma=0.1, kernel="rbf", probability=True)

eclf = VotingClassifier(
    estimators=[("dt", clf1), ("knn", clf2), ("svc", clf3)],
    voting="soft",
    weights=[2, 1, 2],
)

clf1.fit(X, y)
clf2.fit(X, y)
clf3.fit(X, y)
eclf.fit(X, y)
```
