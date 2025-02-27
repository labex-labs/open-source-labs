# Clasificación por Vecinos Más Cercanos

En este paso, exploraremos el concepto de clasificación por vecinos más cercanos y cómo se puede implementar utilizando scikit-learn. Utilizaremos el conjunto de datos iris, que consta de mediciones de diferentes flores de iris.

#### Cargar el Conjunto de Datos Iris

```python
import numpy as np
from sklearn import datasets

iris_X, iris_y = datasets.load_iris(return_X_y=True)
```

#### Dividir los Datos en Conjuntos de Entrenamiento y Prueba

```python
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]
```

#### Crear y Ajustar un Clasificador por Vecinos Más Cercanos

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)
```

#### Hacer Predicciones

```python
predictions = knn.predict(iris_X_test)
```
