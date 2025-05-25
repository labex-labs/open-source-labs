# Definir Dados do Caminho (Path Data)

Definimos os dados do caminho nesta etapa. Os dados do caminho são uma sequência de tuplas que especificam os vértices e códigos do caminho. Usamos a classe `mpath.Path` para criar um objeto `Path` a partir desses dados.

```python
Path = mpath.Path
path_data = [
    (Path.MOVETO, (1.58, -2.57)),
    (Path.CURVE4, (0.35, -1.1)),
    (Path.CURVE4, (-1.75, 2.0)),
    (Path.CURVE4, (0.375, 2.0)),
    (Path.LINETO, (0.85, 1.15)),
    (Path.CURVE4, (2.2, 3.2)),
    (Path.CURVE4, (3, 0.05)),
    (Path.CURVE4, (2.0, -0.5)),
    (Path.CLOSEPOLY, (1.58, -2.57)),
    ]
codes, verts = zip(*path_data)
path = mpath.Path(verts, codes)
```
