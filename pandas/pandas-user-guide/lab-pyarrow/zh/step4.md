# 将 PyArrow 数组转换为 pandas 数据结构

如果你有一个 PyArrow 数组或分块数组（ChunkedArray），可以将其转换为 pandas 数据结构，如 Series、Index 或 DataFrame。

```python
# 创建一个 PyArrow 数组
pa_array = pa.array([{"1": "2"}, {"10": "20"}, None], type=pa.map_(pa.string(), pa.string()))

# 将 PyArrow 数组转换为 pandas Series
ser = pd.Series(pd.arrays.ArrowExtensionArray(pa_array))
```
