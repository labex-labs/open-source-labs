# Diviser les données

Nous allons diviser l'ensemble de données en un ensemble d'entraînement et un ensemble de test. L'ensemble d'entraînement sera utilisé pour entraîner le classifieur SGD, tandis que l'ensemble de test sera utilisé pour évaluer ses performances.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
