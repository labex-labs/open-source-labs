# Instanzdaten

Jede Instanz hat ihre eigenen lokalen Daten.

```python
>>> a.x
2
>>> b.x
10
```

Diese Daten werden durch die `__init__()` initialisiert.

```python
class Player:
    def __init__(self, x, y):
        # Any value stored on `self` is instance data
        self.x = x
        self.y = y
        self.health = 100
```

Es gibt keine Beschränkungen für die Gesamtzahl oder den Typ der gespeicherten Attribute.
