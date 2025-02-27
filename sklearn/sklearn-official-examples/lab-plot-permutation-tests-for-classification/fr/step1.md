# Charger le jeu de données et générer des fonctionnalités aléatoires

Nous utiliserons le jeu de données iris, qui est composé de mesures prises sur 3 types d'iris, et générer des données de fonctionnalités aléatoires (c'est-à-dire 20 fonctionnalités), non corrélées avec les étiquettes de classe dans le jeu de données iris.

```python
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target

n_uncorrelated_features = 20
rng = np.random.RandomState(seed=0)
X_rand = rng.normal(size=(X.shape[0], n_uncorrelated_features))
```
