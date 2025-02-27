# Классификация методом ближайшего соседа

В этом разделе мы изучим концепцию классификации методом ближайшего соседа и узнаем, как ее реализовать с использованием scikit-learn. Мы будем использовать датасет iris, состоящий из измерений различных ирисных цветов.

#### Загрузка датасета iris

```python
import numpy as np
from sklearn import datasets

iris_X, iris_y = datasets.load_iris(return_X_y=True)
```

#### Разделение данных на обучающую и тестовую выборки

```python
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]
```

#### Создание и обучение классификатора методом ближайшего соседа

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)
```

#### Предсказание

```python
predictions = knn.predict(iris_X_test)
```
