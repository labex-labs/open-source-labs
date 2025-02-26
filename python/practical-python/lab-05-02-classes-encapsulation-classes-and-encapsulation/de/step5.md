# Einfache Attribute

Betrachten Sie die folgende Klasse.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Ein überraschendes Merkmal ist, dass Sie die Attribute beliebig auf einen beliebigen Wert setzen können:

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares = 100
>>> s.shares = "hundred"
>>> s.shares = [1, 0, 0]
>>>
```

Sie könnten sich das ansehen und denken, dass Sie zusätzliche Überprüfungen benötigen.

```python
s.shares = '50'     #引发一个TypeError，这是一个字符串
```

Wie würden Sie das tun?
