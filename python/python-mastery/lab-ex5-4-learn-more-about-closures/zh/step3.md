# 挑战：消除名称

修改`typedproperty.py`代码，使得不再需要属性名称：

```python
from typedproperty import String, Integer, Float

class Stock:
    name = String()
    shares = Integer()
    price = Float()
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

提示：要做到这一点，请回忆描述符对象的`__set_name__()`方法，当描述符放在类定义中时会调用该方法。
