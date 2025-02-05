# 使用带参数的 PyArrow 类型

对于接受参数的 PyArrow 类型，你可以将带有这些参数的 PyArrow 类型传入 `ArrowDtype`，以便在 `dtype` 参数中使用。

```python
# 导入 PyArrow
import pyarrow as pa

# 使用 PyArrow 列表类型创建一个 pandas Series
list_str_type = pa.list_(pa.string())
ser = pd.Series([["hello"], ["there"]], dtype=pd.ArrowDtype(list_str_type))
```
