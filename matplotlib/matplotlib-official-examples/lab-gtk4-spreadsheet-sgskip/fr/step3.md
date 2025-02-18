# Tracer les données

Maintenant, vous allez tracer les données en double-cliquant sur une entrée dans la vue d'arbre (treeview).

```python
    def plot_row(self, treeview, path, view_column):
        ind, = path
        points = self.data[ind, :]
        self.line.set_ydata(points)
        self.canvas.draw()
```
