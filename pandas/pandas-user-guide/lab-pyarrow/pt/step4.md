# Convertendo um Array PyArrow para Estruturas de Dados pandas

Se você tiver um PyArrow Array ou ChunkedArray, pode convertê-lo em estruturas de dados pandas como Series, Index ou DataFrame.

```python
# Create a PyArrow array
pa_array = pa.array([{"1": "2"}, {"10": "20"}, None], type=pa.map_(pa.string(), pa.string()))

# Convert the PyArrow array to a pandas Series
ser = pd.Series(pd.arrays.ArrowExtensionArray(pa_array))
```
