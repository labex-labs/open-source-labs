# Declaração `import as`

Você pode alterar o nome de um módulo ao importá-lo:

```python
import math as m
def rectangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y
```

Funciona da mesma forma que uma importação normal. Ele apenas renomeia o módulo naquele arquivo.
