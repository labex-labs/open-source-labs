# Implementieren der Plotfunktionalität

In diesem Schritt implementieren wir die Funktionalität, um die Daten zu plotten, wenn auf eine Zeile doppelgeklickt wird.

```python
def plot_row(self, treeview, path, view_column):
    ind, = path
    points = self.data[ind, :]
    self.line.set_ydata(points)
    self.canvas.draw()
```
