# Aktualisiere das Label-Text bei Mausbewegung

Wir werden den Label-Text aktualisieren, um die x,y-Koordinaten der Maus anzuzeigen, wenn diese über der Achse gezogen wird. Wir erstellen eine Funktion, um den Label-Text zu aktualisieren, und verbinden sie mit dem `motion_notify_event` mithilfe der `mpl_connect()`-Methode.

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```
