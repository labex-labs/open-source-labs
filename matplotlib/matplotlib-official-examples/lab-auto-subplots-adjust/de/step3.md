# Definieren der Zeichnen-Rückruffunktion

Wir werden eine Funktion definieren, die jedes Mal aufgerufen wird, wenn das Diagramm gezeichnet wird. Diese Funktion wird die Begrenzungsfelder der y-Beschriftungen berechnen, bestimmen, ob der Subplot genug Platz für die Beschriftungen lässt, und die Subplot-Parameter gegebenenfalls anpassen.

```python
def on_draw(event):
    bboxes = []
    for label in ax.get_yticklabels():
        # Begrenzungsfeld in Pixeln
        bbox_px = label.get_window_extent()
        # Transformieren in relative Koordinaten der Figur. Dies ist die Umkehrung von
        # transFigure.
        bbox_fig = bbox_px.transformed(fig.transFigure.inverted())
        bboxes.append(bbox_fig)
    # das Begrenzungsfeld, das alle Begrenzungsfelder umschließt, ebenfalls in relativen Koordinaten der Figur
    bbox = mtransforms.Bbox.union(bboxes)
    if fig.subplotpars.left < bbox.width:
        # Verschieben Sie den linken Rand des Subplots nach rechts
        fig.subplots_adjust(left=1.1*bbox.width)  # etwas auffüllen
        fig.canvas.draw()
```
