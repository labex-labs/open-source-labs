# Chargement de l'ensemble de données

Nous allons charger l'ensemble de données du logement californien à partir de Scikit-Learn. Nous n'utiliserons que 2 000 échantillons pour réduire le temps de calcul.

```python
N_SPLITS = 5

rng = np.random.RandomState(0)

X_full, y_full = fetch_california_housing(return_X_y=True)
X_full = X_full[::10]
y_full = y_full[::10]
n_samples, n_features = X_full.shape
```
