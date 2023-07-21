# Redefining an existing method

```python
class MyStock(Stock):
    def cost(self):
        return 1.25 * self.shares * self.price
```

Usage example.

```python
>>> s = MyStock('GOOG', 100, 490.1)
>>> s.cost()
61262.5
>>>
```

The new method takes the place of the old one. The other methods are unaffected. It's tremendous.
