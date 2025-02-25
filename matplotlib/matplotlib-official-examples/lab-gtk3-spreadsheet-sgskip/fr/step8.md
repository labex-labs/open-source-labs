# Implémenter la fonctionnalité de tracé

Dans cette étape, nous allons implémenter la fonctionnalité pour tracer les données lorsqu'une ligne est double-cliquée.

```python
def plot_row(self, treeview, path, view_column):
    ind, = path
    points = self.data[ind, :]
    self.line.set_ydata(points)
    self.canvas.draw()
```
