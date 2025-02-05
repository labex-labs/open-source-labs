# Converting PyArrow Array to pandas Data Structures

If you have a PyArrow Array or ChunkedArray, you can convert it into pandas data structures like Series, Index or DataFrame.

```python
# Create a PyArrow array
pa_array = pa.array([{"1": "2"}, {"10": "20"}, None], type=pa.map_(pa.string(), pa.string()))

# Convert the PyArrow array to a pandas Series
ser = pd.Series(pd.arrays.ArrowExtensionArray(pa_array))
```
