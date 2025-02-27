# 決定木分類器を学習する

まず、scikit-learnの`load_iris`データセットを使って決定木分類器をフィットさせます。このデータセットは、それぞれ50個のインスタンスからなる3つのクラスが含まれており、各クラスはアヤメの植物の種類を指します。データセットを学習用とテスト用に分割し、最大3つの葉ノードを持つ決定木分類器をフィットさせます。

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
