# Create a Custom Unit Class

In this step, we will create a custom unit class - `Foo`. This class will support conversion and different tick formatting depending on the "unit". Here, the "unit" is just a scalar conversion factor.

```python
class Foo:
    def __init__(self, val, unit=1.0):
        self.unit = unit
        self._val = val * unit

    def value(self, unit):
        if unit is None:
            unit = self.unit
        return self._val / unit
```
