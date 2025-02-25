# Crear algunos datos ficticios

A continuación, crearemos algunos datos ficticios para utilizar en nuestros gráficos. Usaremos `numpy.arange` para crear una matriz de valores que van desde 0,01 hasta 10,0 con un paso de 0,01. Luego usaremos `numpy.exp` y `numpy.sin` para crear dos conjuntos de datos.

```python
# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)
```
