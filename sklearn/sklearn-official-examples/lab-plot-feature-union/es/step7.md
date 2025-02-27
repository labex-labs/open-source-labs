# Conjunto de Datos Transformado

Utilizaremos las características combinadas para transformar el conjunto de datos.

```python
X_features = combined_features.fit(X, y).transform(X)
print("Combined space has", X_features.shape[1], "features")
```
