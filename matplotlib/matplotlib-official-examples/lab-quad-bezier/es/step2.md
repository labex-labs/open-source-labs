# Creando la ruta

A continuación, crearemos el objeto `Path` para la curva de Bezier. El objeto `Path` toma una lista de vértices y códigos que especifican el tipo de ruta entre los vértices. En este caso, usaremos un código `MOVETO` para moverse al punto de partida, seguido de dos códigos `CURVE3` para especificar los puntos de control y el punto final, y finalmente un código `CLOSEPOLY` para cerrar la ruta.

```python
Path = mpath.Path

bezier_path = Path([(0, 0), (1, 0), (1, 1), (0, 0)],
                   [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY])
```
