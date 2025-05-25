# Definir a função on_press

Em seguida, definimos uma função chamada on_press que ajustará os limites z e y da segunda janela com base na localização de um clique do mouse na primeira janela.

```python
def on_press(event):
    if event.button != 1:
        return
    x, y = event.xdata, event.ydata
    axzoom.set_xlim(x - 0.1, x + 0.1)
    axzoom.set_ylim(y - 0.1, y + 0.1)
    figzoom.canvas.draw()
```
