# Instance Data

Each instance has its own local data.

```python
>>> a.x
2
>>> b.x
10
```

This data is initialized by the `__init__()`.

```python
class Player:
    def __init__(self, x, y):
        # Any value stored on `self` is instance data
        self.x = x
        self.y = y
        self.health = 100
```

There are no restrictions on the total number or type of attributes stored.
