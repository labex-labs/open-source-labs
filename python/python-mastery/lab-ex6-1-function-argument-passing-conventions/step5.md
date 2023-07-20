# Starting Over

Create a new file `stock.py` (or delete all of your previous code). Start over by defining `Stock` as follows:

```python
# stock.py

from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares
```

Once you've done this, run your `teststock.py` unit tests. You should get a lot of failures, but at least a
handful of the tests should pass.
