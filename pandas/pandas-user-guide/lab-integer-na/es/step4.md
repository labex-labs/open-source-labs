# Manejo de valores faltantes con pandas.NA

La clase `IntegerArray` utiliza `pandas.NA` como su valor escalar faltante. Cuando se selecciona un solo elemento que falta, devolverá `pandas.NA`.

```python
# Crear un IntegerArray con un valor faltante
a = pd.array([1, None], dtype="Int64")

# Seleccionar el segundo elemento que es un valor faltante
missing_value = a[1]
# Salida: <NA>
```
