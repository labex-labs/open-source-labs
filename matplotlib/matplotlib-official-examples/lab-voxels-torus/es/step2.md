# Definir la función de puntos medios

A continuación, definimos una función `midpoints` para calcular los puntos medios de una matriz de coordenadas. Esta función se utilizará más adelante para calcular los puntos medios de `r`, `theta` y `z`.

```python
def midpoints(x):
    sl = ()
    for i in range(x.ndim):
        x = (x[sl + np.index_exp[:-1]] + x[sl + np.index_exp[1:]]) / 2.0
        sl += np.index_exp[:]
    return x
```
