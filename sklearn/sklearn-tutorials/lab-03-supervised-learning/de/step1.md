# Klassifikation mit nächsten Nachbarn

In diesem Schritt werden wir das Konzept der Klassifikation mit nächsten Nachbarn erkunden und sehen, wie es mit scikit-learn implementiert werden kann. Wir werden den Iris-Datensatz verwenden, der aus Messungen verschiedener Iris-Blumen besteht.

#### Lade den Iris-Datensatz

```python
import numpy as np
from sklearn import datasets

iris_X, iris_y = datasets.load_iris(return_X_y=True)
```

#### Teile die Daten in Trainings- und Testsets auf

```python
np.random.seed(0)
indices = np.random.permutation(len(iris_X))
iris_X_train = iris_X[indices[:-10]]
iris_y_train = iris_y[indices[:-10]]
iris_X_test = iris_X[indices[-10:]]
iris_y_test = iris_y[indices[-10:]]
```

#### Erstelle und trainiere einen Klassifikator mit nächsten Nachbarn

```python
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()
knn.fit(iris_X_train, iris_y_train)
```

#### Mache Vorhersagen

```python
predictions = knn.predict(iris_X_test)
```
