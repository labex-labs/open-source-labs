# Generar datos para los diagramas de barras

Ahora generaremos los datos para los diagramas de barras. Crearemos cuatro conjuntos de datos, cada uno con 20 valores. Utilizaremos el método `arange()` de NumPy para crear una matriz de 20 valores y el método `random.rand()` de NumPy para generar valores aleatorios para cada conjunto de datos.

```python
colors = ['r', 'g', 'b', 'y']
yticks = [3, 2, 1, 0]
for c, k in zip(colors, yticks):
    xs = np.arange(20)
    ys = np.random.rand(20)
```
