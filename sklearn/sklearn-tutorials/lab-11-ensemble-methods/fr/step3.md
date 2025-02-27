# Diviser les données

Nous allons diviser les données en ensembles d'entraînement et de test en utilisant la fonction `train_test_split` de scikit-learn.

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```
