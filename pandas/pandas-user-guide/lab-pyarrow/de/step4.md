# Konvertieren eines PyArrow-Arrays in pandas-Datenstrukturen

Wenn Sie ein PyArrow-Array oder -ChunkedArray haben, können Sie es in pandas-Datenstrukturen wie Series, Index oder DataFrame umwandeln.

```python
# Erstelle ein PyArrow-Array
pa_array = pa.array([{"1": "2"}, {"10": "20"}, None], type=pa.map_(pa.string(), pa.string()))

# Konvertiere das PyArrow-Array in eine pandas-Serie
ser = pd.Series(pd.arrays.ArrowExtensionArray(pa_array))
```
