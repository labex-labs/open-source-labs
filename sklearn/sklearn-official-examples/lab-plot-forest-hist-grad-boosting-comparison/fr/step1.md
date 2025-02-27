# Charger l'ensemble de données

Nous allons charger l'ensemble de données sur le logement en Californie à l'aide de la fonction `fetch_california_housing` de scikit-learn. Cet ensemble de données est composé de 20 640 échantillons et de 8 caractéristiques.

```python
from sklearn.datasets import fetch_california_housing

X, y = fetch_california_housing(return_X_y=True, as_frame=True)
n_samples, n_features = X.shape

print(f"L'ensemble de données est composé de {n_samples} échantillons et {n_features} caractéristiques")
```
