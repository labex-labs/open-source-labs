# Charger l'ensemble de données Iris et diviser les données

Nous allons charger l'ensemble de données Iris, qui est un ensemble de données largement utilisé en machine learning pour les tâches de classification. L'ensemble de données contient 150 échantillons de fleurs Iris, avec quatre caractéristiques pour chaque échantillon : longueur du sépale, largeur du sépale, longueur des pétales et largeur des pétales. Nous allons diviser l'ensemble de données en caractéristiques d'entrée et en étiquettes cibles.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# Charger l'ensemble de données Iris
iris = datasets.load_iris()

# Diviser l'ensemble de données en caractéristiques d'entrée et en étiquettes cibles
X = iris.data[:, :2] # Nous n'utiliserons que les deux premières caractéristiques à des fins de visualisation
y = iris.target
```
