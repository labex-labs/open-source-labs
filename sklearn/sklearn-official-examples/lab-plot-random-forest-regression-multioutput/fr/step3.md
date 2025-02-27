# Diviser les données en ensembles d'entraînement et de test

Nous allons diviser nos données en un ensemble d'entraînement de 400 et un ensemble de test de 200 en utilisant la fonction `train_test_split` de scikit-learn.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=400, test_size=200, random_state=4)
```
