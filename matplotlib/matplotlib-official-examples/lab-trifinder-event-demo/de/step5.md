# Interaktivität einrichten

Wir müssen die Interaktivität einrichten, um das Dreieck unter dem Cursor zu aktualisieren. Wir werden das `motion_notify_event` verwenden, um zu erkennen, wenn die Maus über dem Diagramm bewegt wird. Wir werden eine Funktion `on_mouse_move()` erstellen, die das Dreieck unter dem Cursor mithilfe des TriFinder-Objekts erhält, das Polygon mit den Eckpunkten des Dreiecks aktualisiert und den Diagrammtitel mit dem Index des Dreiecks aktualisiert.

```python
def on_mouse_move(event):
    if event.inaxes is None:
        tri = -1
    else:
        tri = trifinder(event.xdata, event.ydata)
    update_polygon(tri)
    ax.set_title(f'Triangle {tri}')
    event.canvas.draw()

fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)
```
