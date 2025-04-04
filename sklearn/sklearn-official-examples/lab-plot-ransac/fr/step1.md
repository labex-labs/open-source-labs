# Importation des bibliothèques et génération des données

Nous allons importer les bibliothèques nécessaires, générer des données aléatoires à l'aide du jeu de données make_regression, et ajouter des valeurs aberrantes aux données.

```python
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model, datasets

# Générer des données
n_samples = 1000
n_outliers = 50

X, y, coef = datasets.make_regression(
    n_samples=n_samples,
    n_features=1,
    n_informative=1,
    noise=10,
    coef=True,
    random_state=0,
)

# Ajouter des données aberrantes
np.random.seed(0)
X[:n_outliers] = 3 + 0.5 * np.random.normal(size=(n_outliers, 1))
y[:n_outliers] = -3 + 10 * np.random.normal(size=n_outliers)
```
