# Crear datos para la visualización

A continuación, crearemos una grilla bidimensional que usaremos para la visualización. Podemos crear una grilla usando la función `meshgrid` en NumPy. La función `meshgrid` crea una grilla de puntos a partir de dos vectores, `x` e `y`, que representan las coordenadas de los puntos de la grilla. Crearemos una grilla de 5x5 puntos usando el siguiente bloque de código:

```python
nrows = 5
ncols = 5
x = np.arange(ncols + 1)
y = np.arange(nrows + 1)
X, Y = np.meshgrid(x, y)
Z = X + Y
```
