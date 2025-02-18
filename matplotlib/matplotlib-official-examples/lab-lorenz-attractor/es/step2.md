# Definir la función de Lorenz

Definimos la función de Lorenz, que toma tres parámetros y devuelve una matriz de tres valores. Utilizamos los valores predeterminados `s = 10`, `r = 28` y `b = 2.667` para los parámetros de Lorenz.

```python
def lorenz(xyz, *, s=10, r=28, b=2.667):
    """
    Parámetros
    ----------
    xyz : similar a una matriz, forma (3,)
       Punto de interés en el espacio tridimensional.
    s, r, b : float
       Parámetros que definen el atractor de Lorenz.

    Devuelve
    -------
    xyz_dot : matriz, forma (3,)
       Valores de las derivadas parciales del atractor de Lorenz en *xyz*.
    """
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])
```
