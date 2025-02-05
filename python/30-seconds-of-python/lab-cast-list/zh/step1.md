# 转换为列表

编写一个函数 `cast_list(val)`，它接受一个值作为参数，并将其作为列表返回。如果该值已经是一个列表，则按原样返回。如果该值不是列表但可迭代，则将其作为列表返回。如果该值不可迭代，则将其作为单元素列表返回。

```python
def cast_list(val):
  return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]
```

```python
cast_list('foo') # ['foo']
cast_list([1]) # [1]
cast_list(('foo', 'bar')) # ['foo', 'bar']
```
