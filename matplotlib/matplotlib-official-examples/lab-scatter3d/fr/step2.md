# Préparez les données

Nous allons générer deux ensembles de données avec des valeurs aléatoires à l'aide de la bibliothèque NumPy. Un ensemble représentera les coordonnées x et y, et l'autre ensemble représentera la coordonnée z.

```python
def randrange(n, vmin, vmax):
    """
    Fonction d'aide pour créer un tableau de nombres aléatoires ayant la forme (n, )
    avec chaque nombre distribué Uniformément(vmin, vmax).
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

n = 100

for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
```
