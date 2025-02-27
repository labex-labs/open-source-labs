# Divisez l'ensemble de données

Avant d'entraîner le classifieur d'arbres de décision, nous devons diviser l'ensemble de données en ensembles d'entraînement et de test. Nous utiliserons 70 % des données pour l'entraînement et 30 % pour les tests.

```python
# Divisez l'ensemble de données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```
