# Aktualisiere das Label mit den Cursorkoordinaten

```python
def update(event):
    if event.xdata is None:
        label.set_markup('Drag mouse over axes for position')
    else:
        label.set_markup(
            f'<span color="#ef0000">x,y=({event.xdata}, {event.ydata})</span>')

fig.canvas.mpl_connect('motion_notify_event', update)
```

Wir erstellen eine Funktion, die das Label mit den x- und y-Koordinaten des Cursors aktualisiert, wenn dieser über den Diagrammen bewegt wird. Wir verbinden die Funktion mit dem `motion_notify_event` der Zeichenfläche.
