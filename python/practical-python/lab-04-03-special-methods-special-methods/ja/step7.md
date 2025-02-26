# 属性アクセス

属性にアクセスし、操作し、管理するための代替方法があります。

```python
getattr(obj, 'name')          # obj.name と同じ
setattr(obj, 'name', value)   # obj.name = value と同じ
delattr(obj, 'name')          # del obj.name と同じ
hasattr(obj, 'name')          # 属性が存在するかどうかをテストする
```

例：

```python
if hasattr(obj, 'x'):
    x = getattr(obj, 'x'):
else:
    x = None
```

*注：`getattr()` には便利なデフォルト値 *arg\* もあります。

```python
x = getattr(obj, 'x', None)
```
