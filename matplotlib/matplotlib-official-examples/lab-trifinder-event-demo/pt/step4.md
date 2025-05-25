# Destacar o Triângulo Sob o Cursor

Queremos destacar o triângulo sob o cursor à medida que o mouse é movido sobre o gráfico. Para fazer isso, criaremos um objeto `Polygon` que será atualizado com os vértices do triângulo sob o cursor. Usaremos `ax.add_patch()` para adicionar o polígono ao gráfico.

```python
from matplotlib.patches import Polygon

polygon = Polygon([[0, 0], [0, 0], [0, 0]], facecolor='y')
ax.add_patch(polygon)
```

Também criaremos uma função `update_polygon()` que atualizará os vértices do polígono com os vértices do triângulo sob o cursor.

```python
def update_polygon(tri):
    if tri == -1:
        points = [0, 0, 0]
    else:
        points = triang.triangles[tri]
    xs = triang.x[points]
    ys = triang.y[points]
    polygon.set_xy(np.column_stack([xs, ys]))
```
