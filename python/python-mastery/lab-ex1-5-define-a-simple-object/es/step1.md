# Definiendo un objeto simple

Crea un archivo `stock.py` y define la siguiente clase:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
```

Una vez que hayas hecho esto, ejecuta tu programa y experimenta con tu nuevo objeto `Stock`:

Nota: Para hacer esto, es posible que tengas que ejecutar python usando la opción `-i`. Por ejemplo:

```bash
python3 -i stock.py
```

```python
>>> s = Stock('GOOG',100,490.10)
>>> s.name
'GOOG'
>>> s.shares
100
>>> s.price
490.1
>>> s.cost()
49010.0
>>> print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
      GOOG        100     490.10
>>> t = Stock('IBM', 50, 91.5)
>>> t.cost()
4575.0
>>>
```
