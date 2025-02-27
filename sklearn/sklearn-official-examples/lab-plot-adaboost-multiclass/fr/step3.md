# Diviser l'ensemble de données

Nous allons diviser l'ensemble de données en ensembles d'entraînement et de test, en utilisant les 3000 premiers échantillons pour l'entraînement et les échantillons restants pour les tests.

```python
n_split = 3000
X_train, X_test = X[:n_split], X[n_split:]
y_train, y_test = y[:n_split], y[n_split:]
```
