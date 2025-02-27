# Diviser les données en ensembles d'entraînement et de test

Nous allons diviser nos données en un ensemble d'entraînement et un ensemble de test, avec 50 % des données dans chaque ensemble.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
```
