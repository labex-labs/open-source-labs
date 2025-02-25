# Crear una barra de colores

Crearemos una barra de colores para mostrar la asignación entre los colores y los valores de `dydx`. Usaremos la función `colorbar` de `matplotlib.pyplot` para crear una barra de colores.

```python
line = plt.gca().add_collection(lc)
plt.colorbar(line)
```
