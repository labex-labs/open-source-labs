# Füge eine neue Methode hinzu

```python
class MyStock(Stock):
    def panic(self):
        self.sell(self.shares)
```

Verwendungsbeispiel.

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.sell(25)
>>> s.shares
75
>>> s.panic()
>>> s.shares
0
>>>
```
