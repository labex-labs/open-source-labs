# Crear el eje x secundario

Crearemos el eje x secundario y convertiremos de frecuencia a período. Usaremos `one_over` como función directa y `inverse` como función inversa.

```python
def one_over(x):
    """Vectorized 1/x, treating x==0 manually"""
    x = np.array(x, float)
    near_zero = np.isclose(x, 0)
    x[near_zero] = np.inf
    x[~near_zero] = 1 / x[~near_zero]
    return x

# la función "1/x" es su propia inversa
inverse = one_over

secax = ax.secondary_xaxis('top', functions=(one_over, inverse))
secax.set_xlabel('período [s]')
```
