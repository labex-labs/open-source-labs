# Definir la función de devolución de llamada de dibujo

Definiremos una función que se llamará cada vez que se dibuje el gráfico. Esta función calculará los cuadros delimitadores de las etiquetas del eje y, determinará si el subgráfico deja suficiente espacio para las etiquetas y ajustará los parámetros del subgráfico si es necesario.

```python
def on_draw(event):
    bboxes = []
    for label in ax.get_yticklabels():
        # Bounding box in pixels
        bbox_px = label.get_window_extent()
        # Transform to relative figure coordinates. This is the inverse of
        # transFigure.
        bbox_fig = bbox_px.transformed(fig.transFigure.inverted())
        bboxes.append(bbox_fig)
    # the bbox that bounds all the bboxes, again in relative figure coords
    bbox = mtransforms.Bbox.union(bboxes)
    if fig.subplotpars.left < bbox.width:
        # Move the subplot left edge more to the right
        fig.subplots_adjust(left=1.1*bbox.width)  # pad a little
        fig.canvas.draw()
```
