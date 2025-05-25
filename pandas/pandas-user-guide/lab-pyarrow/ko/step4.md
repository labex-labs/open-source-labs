# PyArrow Array 를 pandas 데이터 구조로 변환하기

PyArrow Array 또는 ChunkedArray 가 있는 경우, 이를 Series, Index 또는 DataFrame 과 같은 pandas 데이터 구조로 변환할 수 있습니다.

```python
# Create a PyArrow array
pa_array = pa.array([{"1": "2"}, {"10": "20"}, None], type=pa.map_(pa.string(), pa.string()))

# Convert the PyArrow array to a pandas Series
ser = pd.Series(pd.arrays.ArrowExtensionArray(pa_array))
```
