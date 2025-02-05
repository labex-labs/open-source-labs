# PyArrow 操作

PyArrow 数据结构集成是通过 pandas 的 ExtensionArray 接口实现的。在该接口集成到 pandas API 的地方，就存在支持的功能。

```python
# 使用 PyArrow 数据类型创建一个 pandas Series
ser = pd.Series([-1.545, 0.2, None], dtype="float32[pyarrow]")

# 执行各种操作
ser.mean()
ser + ser
ser > (ser + 1)
ser.dropna()
ser.isna()
ser.fillna(0)
```
