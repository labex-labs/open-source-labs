# Crear los cubos y el enlace

Ahora, crearemos los dos cubos y el enlace entre ellos. Lo haremos definiendo tres matrices booleanas que se combinarán en una única matriz booleana. Las dos primeras matrices definen la ubicación de los cubos, mientras que la tercera matriz define la ubicación del enlace.

```python
cube1 = (x < 3) & (y < 3) & (z < 3)
cube2 = (x >= 5) & (y >= 5) & (z >= 5)
link = abs(x - y) + abs(y - z) + abs(z - x) <= 2

voxelarray = cube1 | cube2 | link
```
