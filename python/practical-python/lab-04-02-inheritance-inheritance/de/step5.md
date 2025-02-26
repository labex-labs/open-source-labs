# Neudefinieren einer vorhandenen Methode

```python
class MyStock(Stock):
    def cost(self):
        return 1.25 * self.shares * self.price
```

Verwendungsbeispiel.

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.cost()
61262.5
>>>
```

Die neue Methode ersetzt die alte. Die anderen Methoden bleiben unberührt. Es ist großartig.
