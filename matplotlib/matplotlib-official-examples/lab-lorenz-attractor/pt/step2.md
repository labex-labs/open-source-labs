# Definir a Função Lorenz

Definimos a função Lorenz, que recebe três parâmetros e retorna um array de três valores. Usamos os valores padrão `s=10`, `r=28` e `b=2.667` para os parâmetros de Lorenz.

```python
def lorenz(xyz, *, s=10, r=28, b=2.667):
    """
    Parameters
    ----------
    xyz : array-like, shape (3,)
       Ponto de interesse no espaço tridimensional.
    s, r, b : float
       Parâmetros que definem o atrator de Lorenz.

    Returns
    -------
    xyz_dot : array, shape (3,)
       Valores das derivadas parciais do atrator de Lorenz em *xyz*.
    """
    x, y, z = xyz
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return np.array([x_dot, y_dot, z_dot])
```
