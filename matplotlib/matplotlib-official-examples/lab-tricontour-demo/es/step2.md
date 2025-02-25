# Crear la triangulación

Crearemos la triangulación utilizando `matplotlib.tri.Triangulation`. No es necesario especificar los triángulos, por lo que se creará automáticamente la triangulación de Delaunay de los puntos.

```python
triang = tri.Triangulation(x, y)
```
