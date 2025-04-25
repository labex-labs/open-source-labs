# 最近邻分类

在这一步中，我们将探索最近邻分类的概念，以及如何使用 scikit-learn 来实现它。我们将使用鸢尾花数据集，该数据集包含了不同鸢尾花的测量数据。

#### 加载鸢尾花数据集

```python
import numpy as np
from sklearn import datasets

iris_X, iris_y = datasets.load_iris(return_X_y=True)
```

#### 将数据拆分为训练集和测试集

```python
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]
```

#### 创建并拟合最近邻分类器

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)
```

#### 进行预测

```python
predictions = knn.predict(iris_X_test)
```
