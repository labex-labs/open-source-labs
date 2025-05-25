# Conjunto de Dados Transformado

Usaremos os recursos combinados para transformar o conjunto de dados.

```python
X_features = combined_features.fit(X, y).transform(X)
print("O espaço combinado tem", X_features.shape[1], "recursos")
```
