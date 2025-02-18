# データのプロット

これで、ツリービューのエントリをダブルクリックすることでデータをプロットできます。

```python
    def plot_row(self, treeview, path, view_column):
        ind, = path
        points = self.data[ind, :]
        self.line.set_ydata(points)
        self.canvas.draw()
```
