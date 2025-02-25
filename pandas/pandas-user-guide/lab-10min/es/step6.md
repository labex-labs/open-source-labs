# Operaciones con Datos

Podemos realizar operaciones en los dataframes, como ordenar, aplicar funciones, etc.

```python
# Ordenando por un eje
df.sort_index(axis=1, ascending=False)

# Aplicando una función a los datos
df.apply(np.cumsum)
```
