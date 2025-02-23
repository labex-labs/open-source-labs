# Agregar círculos anclados

En este paso, agregaremos dos círculos a la gráfica usando Objetos Anclados.

```python
def draw_circles(ax):
    """Dibuja círculos en coordenadas de ejes."""
    area = DrawingArea(width=40, height=20)
    area.add_artist(Circle((10, 10), 10, fc="tab:blue"))
    area.add_artist(Circle((30, 10), 5, fc="tab:red"))
    box = AnchoredOffsetbox(
        child=area, loc="upper right", pad=0, frameon=False)
    ax.add_artist(box)

draw_circles(ax)
```
