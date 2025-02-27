# Diviser les données

Nous allons diviser l'ensemble de données en un ensemble d'entraînement et un ensemble de test. L'ensemble d'entraînement sera utilisé pour entraîner le modèle, et l'ensemble de test sera utilisé pour évaluer les performances du modèle.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```
