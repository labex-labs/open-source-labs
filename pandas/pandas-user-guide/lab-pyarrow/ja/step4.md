# PyArrow 配列を pandas のデータ構造に変換する

PyArrow 配列または ChunkedArray を持っている場合、それを Series、Index、DataFrame などの pandas のデータ構造に変換することができます。

```python
# PyArrow 配列を作成
pa_array = pa.array([{"1": "2"}, {"10": "20"}, None], type=pa.map_(pa.string(), pa.string()))

# PyArrow 配列を pandas の Series に変換
ser = pd.Series(pd.arrays.ArrowExtensionArray(pa_array))
```
