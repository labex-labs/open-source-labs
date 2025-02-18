# Crear los Datos

Ahora crearemos algunos datos aleatorios que contendrán valores atípicos (outliers). Usaremos `numpy.random.rand` para generar 30 números aleatorios y luego agregaremos dos valores atípicos a los datos.

```python
np.random.seed(19680801)

pts = np.random.rand(30)*.2
# Ahora creemos dos puntos atípicos que estén lejos de todo.
pts[[3, 14]] +=.8
```
