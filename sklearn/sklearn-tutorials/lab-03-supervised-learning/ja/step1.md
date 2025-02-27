# 最近傍法による分類

このステップでは、最近傍法による分類の概念と、scikit-learnを使ってそれを実装する方法を探ります。さまざまなアヤメの花の測定値からなるアヤメデータセットを使います。

#### アヤメデータセットを読み込む

```python
import numpy as np
from sklearn import datasets

iris_X, iris_y = datasets.load_iris(return_X_y=True)
```

#### データを学習用とテスト用に分割する

```python
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]
```

#### 最近傍法による分類器を作成して適合させる

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)
```

#### 予測を行う

```python
predictions = knn.predict(iris_X_test)
```
