# Herausforderung: Namenselimination

Ändern Sie den Code in `typedproperty.py` so, dass Attributnamen nicht mehr erforderlich sind:

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

Hinweis: Um dies zu tun, erinnern Sie sich an die `__set_name__()`-Methode von Deskriptorobjekten, die aufgerufen wird, wenn Deskriptoren in einer Klassendefinition platziert werden.
