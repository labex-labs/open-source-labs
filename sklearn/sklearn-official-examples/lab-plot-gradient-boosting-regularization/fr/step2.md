# Charger et diviser les données

Nous allons utiliser le jeu de données make_hastie_10_2 et le diviser en ensembles d'entraînement et de test.

```python
X, y = datasets.make_hastie_10_2(n_samples=4000, random_state=1)

# map labels from {-1, 1} to {0, 1}
labels, y = np.unique(y, return_inverse=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8, random_state=0)
```
