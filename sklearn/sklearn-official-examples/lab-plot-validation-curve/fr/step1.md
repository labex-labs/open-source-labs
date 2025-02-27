# Chargement du jeu de données

Nous allons commencer par charger le jeu de données des chiffres à partir de scikit-learn et sélectionner un sous-ensemble des données pour la classification binaire des chiffres 1 et 2.

```python
from sklearn.datasets import load_digits

X, y = load_digits(return_X_y=True)
subset_mask = np.isin(y, [1, 2])  # classification binaire : 1 vs 2
X, y = X[subset_mask], y[subset_mask]
```
