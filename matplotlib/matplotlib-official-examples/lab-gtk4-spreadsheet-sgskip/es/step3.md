# Trazar los datos

Ahora, trazarás los datos haciendo doble clic en una entrada de la vista de árbol (treeview).

```python
    def plot_row(self, treeview, path, view_column):
        ind, = path
        points = self.data[ind, :]
        self.line.set_ydata(points)
        self.canvas.draw()
```
