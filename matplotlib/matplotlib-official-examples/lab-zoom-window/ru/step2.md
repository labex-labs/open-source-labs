# Определение функции on_press

Далее мы определяем функцию под названием on_press, которая будет настраивать пределы z и y второго окна в зависимости от положения клика мыши в первом окне.

```python
def on_press(event):
    if event.button!= 1:
        return
    x, y = event.xdata, event.ydata
    axzoom.set_xlim(x - 0.1, x + 0.1)
    axzoom.set_ylim(y - 0.1, y + 0.1)
    figzoom.canvas.draw()
```
