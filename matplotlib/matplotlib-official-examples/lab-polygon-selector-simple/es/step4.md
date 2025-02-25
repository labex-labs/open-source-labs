# Combinando todo

Vamos a crear un ejemplo completo que incluya tanto la creación de un polígono de manera programática como interactiva.

```python
import matplotlib.pyplot as plt
from matplotlib.widgets import PolygonSelector

# Crear una figura y ejes
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

# Crear un objeto PolygonSelector y agregar vértices
selector1 = PolygonSelector(ax1, lambda *args: None)
selector1.verts = [(0.1, 0.4), (0.5, 0.9), (0.3, 0.2)]

# Trazar el polígono
ax1.add_patch(plt.Polygon(selector1.verts, alpha=0.3))

# Crear otro objeto PolygonSelector para la creación interactiva
selector2 = PolygonSelector(ax2, lambda *args: None)

print("Haga clic en la figura para crear un polígono.")
print("Presione la tecla 'esc' para comenzar un nuevo polígono.")
print("Intente mantener presionada la tecla 'shift' para mover todos los vértices.")
print("Intente mantener presionada la tecla 'ctrl' para mover un solo vértice.")

plt.show()
```
