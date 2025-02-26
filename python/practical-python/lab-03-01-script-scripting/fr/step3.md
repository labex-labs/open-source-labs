# Définir les choses

Les noms doivent toujours être définis avant d'être utilisés par la suite.

```python
def carré(x):
    return x*x

a = 42
b = a + 2     # Exige que `a` soit définie

z = carré(b) # Exige que `carré` et `b` soient définies
```

**L'ordre est important.** Vous mettez presque toujours les définitions de variables et de fonctions vers le haut.
