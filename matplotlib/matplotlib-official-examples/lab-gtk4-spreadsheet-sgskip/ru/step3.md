# Построение графика данных

Теперь вы будете строить график данных, двойным щелчком по записи в древовидном представлении (treeview).

```python
    def plot_row(self, treeview, path, view_column):
        ind, = path
        points = self.data[ind, :]
        self.line.set_ydata(points)
        self.canvas.draw()
```
