# 调整转换

`converters` 参数允许我们定义转换函数来处理更复杂的转换。它接受一个字典，其中列索引或列名作为键，转换函数作为值。

```python
convertfunc = lambda x: float(x.strip(b"%"))/100.
np.genfromtxt(StringIO(data), converters={1: convertfunc})
```
