# Importação `from` module

Isso seleciona símbolos específicos de um módulo e os disponibiliza localmente.

```python
from math import sin, cos

def rectangular(r, theta):
    x = r * cos(theta)
    y = r * sin(theta)
    return x, y
```

Isso permite que partes de um módulo sejam usadas sem ter que digitar o prefixo do módulo. É útil para nomes usados com frequência.
