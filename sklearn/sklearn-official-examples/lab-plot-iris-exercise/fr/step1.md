# Charger les données

Nous commencerons par charger le jeu de données Iris et en sélectionnant seulement les deux premières caractéristiques à des fins de visualisation.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, svm

iris = datasets.load_iris()
X = iris.data
y = iris.target

X = X[y!= 0, :2]
y = y[y!= 0]
```
