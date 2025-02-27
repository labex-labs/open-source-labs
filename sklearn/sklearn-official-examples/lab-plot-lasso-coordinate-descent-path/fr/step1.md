# Charger l'ensemble de données

Dans cette étape, nous allons charger l'ensemble de données sur le diabète provenant de la bibliothèque scikit-learn et standardiser les données.

```python
from sklearn import datasets

# Charger l'ensemble de données sur le diabète
X, y = datasets.load_diabetes(return_X_y=True)

# Standardiser les données
X /= X.std(axis=0)
```
