# Creando datos para el trazado

En este paso, crearemos datos para trazar en un diagrama de contorno. Utilizamos la función `np.meshgrid()` para crear una cuadrícula de puntos y luego calculamos los valores de `z` utilizando las funciones seno y coseno.

```python
# Data to plot.
x, y = np.meshgrid(np.arange(7), np.arange(10))
z = np.sin(0.5 * x) * np.cos(0.52 * y)
```
