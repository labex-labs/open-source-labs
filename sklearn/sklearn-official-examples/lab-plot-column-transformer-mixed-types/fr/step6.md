# Diviser les données

Dans cette étape, nous allons diviser nos données en ensembles d'entraînement et de test en utilisant `train_test_split`.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
```
