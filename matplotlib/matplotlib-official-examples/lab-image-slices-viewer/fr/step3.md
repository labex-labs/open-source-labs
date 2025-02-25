# Créez la classe IndexTracker

La classe `IndexTracker` suivra l'index de la tranche actuelle et mettra à jour le tracé en conséquence.

```python
class IndexTracker:
    def __init__(self, ax, X):
        self.index = 0
        self.X = X
        self.ax = ax
        self.im = ax.imshow(self.X[:, :, self.index])
        self.update()

    def on_scroll(self, event):
        increment = 1 if event.button == 'up' else -1
        max_index = self.X.shape[-1] - 1
        self.index = np.clip(self.index + increment, 0, max_index)
        self.update()

    def update(self):
        self.im.set_data(self.X[:, :, self.index])
        self.ax.set_title(
            f'Utilisez la molette de la souris pour naviguer\nindex {self.index}')
        self.im.axes.figure.canvas.draw()
```
