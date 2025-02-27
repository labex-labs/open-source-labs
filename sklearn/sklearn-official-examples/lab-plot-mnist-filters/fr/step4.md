# Diviser les données

Nous allons diviser l'ensemble de données en un ensemble d'entraînement et un ensemble de test à l'aide de la fonction `train_test_split`.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.7)
```
