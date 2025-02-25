# Définir la fonction on_press

Ensuite, nous définissons une fonction appelée on_press qui ajustera les limites x et y de la deuxième fenêtre en fonction de l'emplacement d'un clic de souris dans la première fenêtre.

```python
def on_press(event):
    if event.button!= 1:
        return
    x, y = event.xdata, event.ydata
    axzoom.set_xlim(x - 0.1, x + 0.1)
    axzoom.set_ylim(y - 0.1, y + 0.1)
    figzoom.canvas.draw()
```
