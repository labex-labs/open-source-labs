# Datos de instancia

Cada instancia tiene sus propios datos locales.

```python
>>> a.x
2
>>> b.x
10
```

Estos datos se inicializan por el método `__init__()`.

```python
class Player:
    def __init__(self, x, y):
        # Cualquier valor almacenado en `self` es datos de instancia
        self.x = x
        self.y = y
        self.health = 100
```

No hay restricciones sobre el número total o el tipo de atributos almacenados.
