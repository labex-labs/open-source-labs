# Criando os Vértices e Códigos

Criaremos os vértices e códigos para os dois polígonos que queremos combinar em um caminho composto. Usaremos `Path.MOVETO` para mover o cursor para o ponto inicial do polígono, `Path.LINETO` para criar uma linha do ponto inicial para o próximo ponto e `Path.CLOSEPOLY` para fechar o polígono.

```python
vertices = []
codes = []

# First Polygon - Rectangle
codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
vertices = [(1, 1), (1, 2), (2, 2), (2, 1), (0, 0)]

# Second Polygon - Triangle
codes += [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]
vertices += [(4, 4), (5, 5), (5, 4), (0, 0)]
```
