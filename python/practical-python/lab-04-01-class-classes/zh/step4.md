# 实例数据

每个实例都有自己的局部数据。

```python
>>> a.x
2
>>> b.x
10
```

此数据由 `__init__()` 初始化。

```python
class Player:
    def __init__(self, x, y):
        # 存储在 `self` 上的任何值都是实例数据
        self.x = x
        self.y = y
        self.health = 100
```

对于所存储的属性的总数或类型没有限制。
