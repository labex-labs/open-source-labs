# Преобразование массива PyArrow в структуры данных pandas

Если у вас есть массив PyArrow или ChunkedArray, вы можете преобразовать его в структуры данных pandas, такие как Series, Index или DataFrame.

```python
# Создать массив PyArrow
pa_array = pa.array([{"1": "2"}, {"10": "20"}, None], type=pa.map_(pa.string(), pa.string()))

# Преобразовать массив PyArrow в pandas Series
ser = pd.Series(pd.arrays.ArrowExtensionArray(pa_array))
```
