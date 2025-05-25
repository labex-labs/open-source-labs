# Definir a função de retorno de chamada (callback) de desenho

Vamos definir uma função que será chamada toda vez que o gráfico for desenhado. Esta função calculará as caixas delimitadoras (bounding boxes) dos rótulos y, determinará se o subplot deixa espaço suficiente para os rótulos e ajustará os parâmetros do subplot, se necessário.

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
