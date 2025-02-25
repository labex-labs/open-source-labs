# Creando los vértices y los códigos

Crearemos los vértices y los códigos para los dos polígonos que queremos combinar en un camino compuesto. Usaremos `Path.MOVETO` para mover el cursor al punto de inicio del polígono, `Path.LINETO` para crear una línea desde el punto de inicio hasta el siguiente punto y `Path.CLOSEPOLY` para cerrar el polígono.

```python
vertices = []
codes = []

# Primer polígono - Rectángulo
codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
vertices = [(1, 1), (1, 2), (2, 2), (2, 1), (0, 0)]

# Segundo polígono - Triángulo
codes += [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]
vertices += [(4, 4), (5, 5), (5, 4), (0, 0)]
```
