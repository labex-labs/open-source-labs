# Implementar a Funcionalidade de Plotagem

Nesta etapa, implementaremos a funcionalidade para plotar os dados quando uma linha for clicada duas vezes.

```python
def plot_row(self, treeview, path, view_column):
    ind, = path
    points = self.data[ind, :]
    self.line.set_ydata(points)
    self.canvas.draw()
```
