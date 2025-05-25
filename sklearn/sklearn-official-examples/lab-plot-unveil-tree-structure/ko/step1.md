# 의사결정 트리 분류기 학습

먼저, scikit-learn 의 `load_iris` 데이터셋을 사용하여 의사결정 트리 분류기를 학습해야 합니다. 이 데이터셋은 각각 50 개의 인스턴스를 가진 3 개의 클래스로 구성되어 있으며, 각 클래스는 아이리스 식물의 한 유형을 나타냅니다. 데이터셋을 학습용과 테스트용으로 분할하고 최대 3 개의 잎 노드를 가진 의사결정 트리 분류기를 학습할 것입니다.

```python
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

clf = DecisionTreeClassifier(max_leaf_nodes=3, random_state=0)
clf.fit(X_train, y_train)
```
