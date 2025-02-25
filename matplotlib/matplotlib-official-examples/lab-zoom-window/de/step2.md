# Definieren der on_press-Funktion

Als nächstes definieren wir eine Funktion namens on_press, die die x- und y-Bereiche des zweiten Fensters basierend auf der Position eines Mausklicks im ersten Fenster anpasst.

```python
def on_press(event):
    if event.button!= 1:
        return
    x, y = event.xdata, event.ydata
    axzoom.set_xlim(x - 0.1, x + 0.1)
    axzoom.set_ylim(y - 0.1, y + 0.1)
    figzoom.canvas.draw()
```
