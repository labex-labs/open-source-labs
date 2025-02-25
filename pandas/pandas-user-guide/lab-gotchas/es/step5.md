# Comprendiendo las diferencias con NumPy

Pandas y NumPy tienen ligeras diferencias en cómo calculan la varianza. Es importante tener en cuenta esto al cambiar entre las dos bibliotecas.

```python
# Varianza en pandas
var_pandas = df.var()

# Varianza en NumPy
var_numpy = np.var(df.values)
```
