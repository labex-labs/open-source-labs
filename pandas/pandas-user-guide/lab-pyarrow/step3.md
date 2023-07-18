# Using PyArrow Types with Parameters

For PyArrow types that accept parameters, you can pass in a PyArrow type with those parameters into `ArrowDtype` to use in the `dtype` parameter.

```python
# Import PyArrow
import pyarrow as pa

# Create a pandas Series with PyArrow list type
list_str_type = pa.list_(pa.string())
ser = pd.Series([["hello"], ["there"]], dtype=pd.ArrowDtype(list_str_type))
```
