# Instruction `import as`

Vous pouvez modifier le nom d'un module lors de son importation :

```python
import math as m
def rectangular(r, theta):
    x = r * m.cos(theta)
    y = r * m.sin(theta)
    return x, y
```

Ça fonctionne de la même manière qu'un import normal. Il ne fait que renommer le module dans ce fichier-là.
