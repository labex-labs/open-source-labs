# Conversion d'un tableau PyArrow en structures de données pandas

Si vous avez un tableau PyArrow ou un ChunkedArray, vous pouvez le convertir en structures de données pandas telles que Series, Index ou DataFrame.

```python
# Créez un tableau PyArrow
pa_array = pa.array([{"1": "2"}, {"10": "20"}, None], type=pa.map_(pa.string(), pa.string()))

# Convertissez le tableau PyArrow en une série pandas
ser = pd.Series(pd.arrays.ArrowExtensionArray(pa_array))
```
