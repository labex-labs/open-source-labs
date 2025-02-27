# Charger et préparer les données

Nous commençons par importer les bibliothèques nécessaires et charger l'ensemble de données iris. Nous allons ensuite mélanger les données et les standardiser pour les utiliser dans l'entraînement.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import SGDClassifier

# charger l'ensemble de données iris
iris = datasets.load_iris()

# prendre les deux premières caractéristiques
X = iris.data[:, :2]
y = iris.target
couleurs = "bry"

# mélanger les données
idx = np.arange(X.shape[0])
np.random.seed(13)
np.random.shuffle(idx)
X = X[idx]
y = y[idx]

# standardiser les données
moyenne = X.mean(axis=0)
écart_type = X.std(axis=0)
X = (X - moyenne) / écart_type
```
