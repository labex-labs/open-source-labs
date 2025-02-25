# Définir la fonction des points moyens

Ensuite, nous définissons une fonction `midpoints` pour calculer les points moyens d'un tableau de coordonnées. Cette fonction sera utilisée plus tard pour calculer les points moyens de `r`, `theta` et `z`.

```python
def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
