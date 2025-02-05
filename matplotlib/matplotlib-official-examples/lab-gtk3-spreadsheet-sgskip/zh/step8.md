# 实现绘图功能

在这一步中，我们将实现双击某一行时绘制数据的功能。

```python
def plot_row(self, treeview, path, view_column):
    ind, = path
    points = self.data[ind, :]
    self.line.set_ydata(points)
    self.canvas.draw()
```
