# 绘制数据

现在，你将通过双击树状视图中的条目来绘制数据。

```python
    def plot_row(self, treeview, path, view_column):
        ind, = path
        points = self.data[ind, :]
        self.line.set_ydata(points)
        self.canvas.draw()
```
