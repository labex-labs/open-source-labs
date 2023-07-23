# Nearest Neighbor Classification

In this step, we will explore the concept of nearest neighbor classification and how it can be implemented using scikit-learn. We will use the iris dataset, which consists of measurements of different iris flowers.

#### Load the Iris Dataset

```python
import numpy as np
from sklearn import datasets

iris_X, iris_y = datasets.load_iris(return_X_y=True)
```

#### Split the Data into Train and Test Sets

```python
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]
```

#### Create and Fit a Nearest Neighbor Classifier

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)
```

#### Make Predictions

```python
predictions = knn.predict(iris_X_test)
```
