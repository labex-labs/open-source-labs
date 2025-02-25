# Crear datos de ejemplo

A continuación, crearemos datos de ejemplo para utilizar en el gráfico. En este ejemplo, usaremos la función `numpy.arange()` para crear una matriz de valores entre 0,1 y 4 con un paso de 0,5. Luego usaremos la función `numpy.exp()` para calcular el exponencial de cada valor en la matriz.

```python
# example data
x = np.arange(0.1, 4, 0.5)
y = np.exp(-x)
```
