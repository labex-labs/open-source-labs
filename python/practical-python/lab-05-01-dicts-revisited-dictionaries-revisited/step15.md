# The "Mixin" Pattern

The _Mixin_ pattern is a class with a fragment of code.

```python
class Loud:
    def noise(self):
        return super().noise().upper()
```

This class is not usable in isolation. It mixes with other classes via inheritance.

```python
class LoudDog(Loud, Dog):
    pass

class LoudBike(Loud, Bike):
    pass
```

Miraculously, loudness was now implemented just once and reused in two completely unrelated classes. This sort of trick is one of the primary uses of multiple inheritance in Python.
