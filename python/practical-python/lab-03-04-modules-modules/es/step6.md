# Sentencia `import as`

Puedes cambiar el nombre de un módulo al importarlo:

```python
import math as m
def rectangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y
```

Funciona de la misma manera que una importación normal. Simplemente renombra el módulo en ese archivo.
