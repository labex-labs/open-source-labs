# Juntando Tudo

Vamos criar um exemplo completo que inclui tanto a criação de um polígono programaticamente quanto interativamente.

```python
import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector

# Create a figure and axes
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

# Create a PolygonSelector object and add vertices
selector1 = PolygonSelector(ax1, lambda *args: None)
selector1.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# Plot the polygon
ax1.add_patch(plt.Polygon(selector1.verts, alpha=0.3))

# Create another PolygonSelector object for interactive creation
selector2 = PolygonSelector(ax2, lambda *args: None)

print("Clique na figura para criar um polígono.")
print("Pressione a tecla 'esc' para iniciar um novo polígono.")
print("Tente segurar a tecla 'shift' para mover todos os vértices.")
print("Tente segurar a tecla 'ctrl' para mover um único vértice.")

plt.show()
```
