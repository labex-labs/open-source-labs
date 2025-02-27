# Diviser les données

Nous allons diviser les données en un ensemble d'entraînement et un ensemble de test.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```
