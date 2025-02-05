# 修正名称

描述符有一个令人烦恼的地方，就是名称规范冗余。例如：

```python
class Stock:
  ...
    shares = PositiveInteger('shares')
  ...
```

我们可以解决这个问题。将顶级的`Validator`类修改为包含一个`__set_name__()`方法，如下所示：

```python
# validate.py

class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)
```

现在，尝试重写你的`Stock`类，使其如下所示：

```python
class Stock:
    name   = String()
    shares = PositiveInteger()
    price  = PositiveFloat()

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
```

啊，好多了。不过要注意，设置名称的这个功能是Python 3.6的特性。在旧版本中无法使用。
