# Plot the Data

Now, you will plot the data by double-clicking on an entry in the treeview.

```python
    def plot_row(self, treeview, path, view_column):
        ind, = path
        points = self.data[ind, :]
        self.line.set_ydata(points)
        self.canvas.draw()
```
