# Classification par plus proche voisin

Dans cette étape, nous explorerons le concept de classification par plus proche voisin et comment il peut être implémenté à l'aide de scikit-learn. Nous utiliserons l'ensemble de données iris, qui consiste en des mesures de différentes fleurs d'iris.

#### Charger l'ensemble de données Iris

```python
import numpy as np
from sklearn import datasets

iris_X, iris_y = datasets.load_iris(return_X_y=True)
```

#### Diviser les données en ensembles d'entraînement et de test

```python
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]
```

#### Créer et ajuster un classifieur par plus proche voisin

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)
```

#### Faire des prédictions

```python
predictions = knn.predict(iris_X_test)
```
