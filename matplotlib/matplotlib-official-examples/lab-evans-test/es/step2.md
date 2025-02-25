# Crear una clase de unidad personalizada

En este paso, crearemos una clase de unidad personalizada: `Foo`. Esta clase soportará la conversión y diferentes formatos de marcas de graduación según la "unidad". Aquí, la "unidad" es simplemente un factor de conversión escalar.

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
