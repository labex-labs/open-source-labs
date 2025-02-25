# Créer une classe d'unité personnalisée

Dans cette étape, nous allons créer une classe d'unité personnalisée - `Foo`. Cette classe prendra en charge la conversion et différents formats d'étiquetage en fonction de l'"unité". Ici, l'"unité" est simplement un facteur de conversion scalaire.

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
