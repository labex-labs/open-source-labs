# Criar os cubos e a ligação

Agora, criaremos os dois cubos e a ligação entre eles. Faremos isso definindo três arrays booleanos que serão combinados em um único array booleano. Os dois primeiros arrays definem a localização dos cubos, enquanto o terceiro array define a localização da ligação.

```python
cube1 = (x < 3) & (y < 3) & (z < 3)
cube2 = (x >= 5) & (y >= 5) & (z >= 5)
link = abs(x - y) + abs(y - z) + abs(z - x) <= 2

voxelarray = cube1 | cube2 | link
```
