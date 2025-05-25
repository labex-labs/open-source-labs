# Plotar os Dados

Agora, você irá plotar os dados ao dar um duplo clique em uma entrada na treeview.

```python
    def plot_row(self, treeview, path, view_column):
        ind, = path
        points = self.data[ind, :]
        self.line.set_ydata(points)
        self.canvas.draw()
```
