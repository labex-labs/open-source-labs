# 描画機能を実装する

このステップでは、行をダブルクリックしたときにデータを描画する機能を実装します。

```python
def plot_row(self, treeview, path, view_column):
    ind, = path
    points = self.data[ind, :]
    self.line.set_ydata(points)
    self.canvas.draw()
```
