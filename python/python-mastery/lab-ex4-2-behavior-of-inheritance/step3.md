# Using your validators

Your validators can be used to add value checking to functions and classes. For example, perhaps the validators could be used in the properties of `Stock`:

```python
class Stock:
    ...
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        self._shares = PositiveInteger.check(value)
    ...
```

Copy the `Stock` class from `stock.py` change it to use the validators in the property code for `shares` and `price`.
