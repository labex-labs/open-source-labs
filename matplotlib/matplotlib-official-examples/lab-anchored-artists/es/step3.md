# Agregar texto anclado

En este paso, agregaremos un cuadro de texto anclado a la esquina superior izquierda de la figura.

```python
def draw_text(ax):
    """Dibuja un cuadro de texto anclado a la esquina superior izquierda de la figura."""
    box = AnchoredOffsetbox(child=TextArea("Figure 1a"),
                            loc="upper left", frameon=True)
    box.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
    ax.add_artist(box)

draw_text(ax)
```
