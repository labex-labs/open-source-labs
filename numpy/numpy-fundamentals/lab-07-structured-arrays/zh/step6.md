# 创建记录数组

记录数组是ndarray的一个子类，它允许通过属性而非索引来访问字段。我们可以使用`np.rec.array`函数创建一个记录数组。

```python
# 创建一个记录数组
recordarr = np.rec.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```
