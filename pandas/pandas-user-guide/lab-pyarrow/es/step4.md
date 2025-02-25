# Convertir una Matriz de PyArrow a Estructuras de Datos de pandas

Si tienes una Matriz de PyArrow o una ChunkedArray de PyArrow, puedes convertirla en estructuras de datos de pandas como Series, Índice o DataFrame.

```python
# Crea una matriz de PyArrow
pa_array = pa.array([{"1": "2"}, {"10": "20"}, None], type=pa.map_(pa.string(), pa.string()))

# Convierte la matriz de PyArrow en una Serie de pandas
ser = pd.Series(pd.arrays.ArrowExtensionArray(pa_array))
```
