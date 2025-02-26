# `from` módulo importar

Esto selecciona símbolos específicos de un módulo y los hace disponibles localmente.

```python
from math import sin, cos

def rectangular(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y
```

Esto permite utilizar partes de un módulo sin tener que escribir el prefijo del módulo. Es útil para nombres que se utilizan con frecuencia.
