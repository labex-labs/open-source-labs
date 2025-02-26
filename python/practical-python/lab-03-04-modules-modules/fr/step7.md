# Importation à partir d'un module (`from`)

Cela permet de sélectionner des symboles d'un module et de les rendre disponibles localement.

```python
from math import sin, cos

def rectangular(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y
```

Cela permet d'utiliser des parties d'un module sans avoir à taper le préfixe du module. C'est pratique pour les noms utilisés fréquemment.
