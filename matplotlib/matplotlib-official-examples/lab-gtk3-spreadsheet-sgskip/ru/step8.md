# Реализуйте функциональность построения графика

В этом шаге мы реализуем функциональность для построения графика данных при двойном щелчке по строке.

```python
def plot_row(self, treeview, path, view_column):
    ind, = path
    points = self.data[ind, :]
    self.line.set_ydata(points)
    self.canvas.draw()
```
