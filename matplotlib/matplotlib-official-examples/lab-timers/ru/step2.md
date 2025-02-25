# Определить функцию для обновления заголовка

Определите функцию для обновления заголовка рисунка текущим временем.

```python
def update_title(axes):
    axes.set_title(datetime.now())
    axes.figure.canvas.draw()
```
