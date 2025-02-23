# Agregar elipse anclada

En este paso, agregaremos una elipse a la gráfica usando Objetos Anclados.

```python
def draw_ellipse(ax):
    """Dibuja una elipse de ancho = 0,1, alto = 0,15 en coordenadas de datos."""
    aux_tr_box = AuxTransformBox(ax.transData)
    aux_tr_box.add_artist(Ellipse((0, 0), width=0.1, height=0.15))
    box = AnchoredOffsetbox(child=aux_tr_box, loc="lower left", frameon=True)
    ax.add_artist(box)

draw_ellipse(ax)
```
