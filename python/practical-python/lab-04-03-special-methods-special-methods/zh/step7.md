# 属性访问

存在另一种访问、操作和管理属性的方式。

```python
getattr(obj, 'name')          # 与 obj.name 相同
setattr(obj, 'name', value)   # 与 obj.name = value 相同
delattr(obj, 'name')          # 与 del obj.name 相同
hasattr(obj, 'name')          # 测试属性是否存在
```

示例：

```python
if hasattr(obj, 'x'):
    x = getattr(obj, 'x'):
else:
    x = None
```

*注意：`getattr()` 还有一个有用的默认值 *arg\*。

```python
x = getattr(obj, 'x', None)
```
