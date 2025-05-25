# Criar a região sombreada

Crie a região sombreada usando um patch `Polygon`. Gere valores de x e y para a região usando `linspace` e a função definida no passo 1. Em seguida, defina os vértices da região como uma lista de tuplas. Finalmente, crie o objeto `Polygon` e adicione-o ao eixo usando `add_patch`.

```python
from matplotlib.patches import Polygon

ix = np.linspace(a, b)
iy = func(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
ax.add_patch(poly)
```
