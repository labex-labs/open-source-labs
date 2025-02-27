# Prétraitement des données

Avant d'appliquer la SGD, il est souvent avantageux de prétraiter les données. Dans ce cas, nous allons standardiser les caractéristiques à l'aide de StandardScaler de scikit-learn.

```python
scaler = StandardScaler()
X = scaler.fit_transform(X)
```
