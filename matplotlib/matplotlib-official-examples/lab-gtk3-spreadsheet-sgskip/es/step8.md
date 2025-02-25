# Implementar la funcionalidad de trazado

En este paso, implementaremos la funcionalidad para trazar los datos cuando se hace doble clic en una fila.

```python
def plot_row(self, treeview, path, view_column):
    ind, = path
    points = self.data[ind, :]
    self.line.set_ydata(points)
    self.canvas.draw()
```
