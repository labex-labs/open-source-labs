# Ein einfaches Objekt definieren

Erstellen Sie eine Datei `stock.py` und definieren Sie die folgende Klasse:

```python
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
```

Sobald Sie dies getan haben, führen Sie Ihr Programm aus und experimentieren Sie mit Ihrem neuen `Stock`-Objekt:

Hinweis: Um dies zu tun, müssen Sie möglicherweise Python mit der Option `-i` ausführen. Beispielsweise:

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
