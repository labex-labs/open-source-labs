# 设置数据类型

`dtype` 参数用于控制字符串如何转换为其他类型。它可以是单个类型、类型序列、逗号分隔的字符串、字典、元组序列、现有的 `numpy.dtype` 对象，或者为 `None` 以根据数据本身确定类型。

```python
np.genfromtxt(StringIO(data), dtype=float)
```
