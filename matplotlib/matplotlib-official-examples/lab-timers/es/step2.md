# Definir la función para actualizar el título

Definir la función para actualizar el título de la figura con la hora actual.

```python
def update_title(axes):
    axes.set_title(datetime.now())
    axes.figure.canvas.draw()
```
