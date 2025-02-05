# 实例方法

实例方法是应用于对象实例的函数。

```python
class Player:
  ...
    # `move` 是一个方法
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
```

对象本身总是作为第一个参数传递。

```python
>>> a.move(1, 2)

# 将 `a` 匹配到 `self`
# 将 `1` 匹配到 `dx`
# 将 `2` 匹配到 `dy`
def move(self, dx, dy):
```

按照惯例，实例被称为 `self`。然而，实际使用的名称并不重要。对象总是作为第一个参数传递。将这个参数称为 `self` 只是 Python 的编程风格。
