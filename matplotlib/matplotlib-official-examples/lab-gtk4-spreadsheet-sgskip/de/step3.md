# Plotten der Daten

Nun werden Sie die Daten plotten, indem Sie auf einen Eintrag in der Treeview (Baumansicht) doppelt klicken.

```python
    def plot_row(self, treeview, path, view_column):
        ind, = path
        points = self.data[ind, :]
        self.line.set_ydata(points)
        self.canvas.draw()
```
