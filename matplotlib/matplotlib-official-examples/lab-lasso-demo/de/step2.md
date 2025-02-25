# Erstellen der LassoManager-Klasse

Als nächstes erstellen wir die `LassoManager`-Klasse, die die Lasso-Funktionalität behandelt. Die `__init__`-Methode initialisiert das Plot- und das Collection-Objekt. Die `callback`-Methode ändert die Farbe der ausgewählten Punkte, und die `on_press`- und `on_release`-Methoden behandeln die Mausereignisse.

```python
class LassoManager:
    def __init__(self, ax, data):
        # Die Information darüber, ob ein Punkt ausgewählt wurde oder nicht, wird im
        # Array der Collection gespeichert (0 = draußen, 1 = drinnen), das dann
        # farbzugeordnet wird zu blau (draußen) und rot (drinnen).
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
        canvas.widgetlock(self.lasso)  # erhalte ein Sperrrecht auf das Widget-Zeichnen

    def on_release(self, event):
        canvas = self.collection.figure.canvas
        if hasattr(self, 'lasso') and canvas.widgetlock.isowner(self.lasso):
            canvas.widgetlock.release(self.lasso)
```
