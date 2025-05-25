# Definir as linhas de contorno e polígonos

O próximo passo é definir as linhas de contorno e os polígonos. Neste exemplo, temos linhas e contornos preenchidos entre dois níveis.

```python
# As linhas de contorno para cada nível são uma lista/tupla de polígonos.
lines0 = [[[0, 0], [0, 4]]]
lines1 = [[[2, 0], [1, 2], [1, 3]]]
lines2 = [[[3, 0], [3, 2]], [[3, 3], [3, 4]]]  # Note two lines.

# Contornos preenchidos entre dois níveis também são uma lista/tupla de polígonos.
# Os pontos podem ser ordenados no sentido horário ou anti-horário.
filled01 = [[[0, 0], [0, 4], [1, 3], [1, 2], [2, 0]]]
filled12 = [[[2, 0], [3, 0], [3, 2], [1, 3], [1, 2]],   # Note two polygons.
            [[1, 4], [3, 4], [3, 3]]]
```
