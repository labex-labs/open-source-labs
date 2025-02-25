# Definir la función on_press

A continuación, definimos una función llamada on_press que ajustará los límites z y y de la segunda ventana en función de la ubicación de un clic del mouse en la primera ventana.

```python
def on_press(event):
    if event.button!= 1:
        return
    x, y = event.xdata, event.ydata
    axzoom.set_xlim(x - 0.1, x + 0.1)
    axzoom.set_ylim(y - 0.1, y + 0.1)
    figzoom.canvas.draw()
```
