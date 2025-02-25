# Créer la classe LassoManager

Ensuite, créez la classe `LassoManager` qui gérera la fonctionnalité du lasso. La méthode `__init__` initialise l'objet de tracé et de collection. La méthode `callback` change la couleur des points sélectionnés, et les méthodes `on_press` et `on_release` gèrent les événements de souris.

```python
class LassoManager:
    def __init__(self, ax, data):
        # L'information sur le fait qu'un point a été sélectionné ou non est stockée dans le
        # tableau de la collection (0 = hors, 1 = dans), qui est ensuite coloré en bleu
        # (hors) et en rouge (dans).
        self.collection = RegularPolyCollection(
            6, sizes=(100,), offset_transform=ax.transData,
            offsets=data, array=np.zeros(len(data)),
            clim=(0, 1), cmap=mcolors.ListedColormap(["tab:blue", "tab:red"]))
        ax.add_collection(self.collection)
        canvas = ax.figure.canvas
        canvas.mpl_connect('button_press_event', self.on_press)
        canvas.mpl_connect('button_release_event', self.on_release)

    def callback(self, verts):
        data = self.collection.get_offsets()
        self.collection.set_array(path.Path(verts).contains_points(data))
        canvas = self.collection.figure.canvas
        canvas.draw_idle()
        del self.lasso

    def on_press(self, event):
        canvas = self.collection.figure.canvas
        if event.inaxes is not self.collection.axes or canvas.widgetlock.locked():
            return
        self.lasso = Lasso(event.inaxes, (event.xdata, event.ydata), self.callback)
        canvas.widgetlock(self.lasso)  # acquérir un verrou sur le dessin du widget

    def on_release(self, event):
        canvas = self.collection.figure.canvas
        if hasattr(self, 'lasso') and canvas.widgetlock.isowner(self.lasso):
            canvas.widgetlock.release(self.lasso)
```
