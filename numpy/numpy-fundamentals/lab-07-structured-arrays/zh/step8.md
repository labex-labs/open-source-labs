# 将结构化数组转换为记录数组

我们可以使用`view`方法并指定`np.recarray`类型，将结构化数组转换为记录数组。

```python
# 将结构化数组转换为记录数组
recordarr = x.view(np.recarray)
```
