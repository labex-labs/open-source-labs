# Atributos Simples

Considere a seguinte classe.

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
```

Uma característica surpreendente é que você pode definir os atributos para qualquer valor:

```python
>>> s = Stock('IBM', 50, 91.1)
>>> s.shares = 100
>>> s.shares = "hundred"
>>> s.shares = [1, 0, 0]
>>>
```

Você pode olhar para isso e pensar que precisa de algumas verificações extras.

```python
s.shares = '50'     # Raise a TypeError, this is a string
```

Como você faria isso?
