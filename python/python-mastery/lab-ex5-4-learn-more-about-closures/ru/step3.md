# Вызов к действию: устранение имен

Измените код в `typedproperty.py` так, чтобы имена атрибутов больше не были обязательными:

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

Совет: Для этого вспомните метод `__set_name__()` дескрипторных объектов, который вызывается, когда дескрипторы размещаются в определении класса.
