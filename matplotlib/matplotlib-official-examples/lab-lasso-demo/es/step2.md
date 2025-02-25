# Crear la clase LassoManager

A continuación, cree la clase `LassoManager` que manejará la funcionalidad del lasso. El método `__init__` inicializa el objeto de trama y colección. El método `callback` cambia el color de los puntos seleccionados, y los métodos `on_press` y `on_release` manejan los eventos del mouse.

```python
class LassoManager:
    def __init__(self, ax, data):
        # La información de si un punto ha sido seleccionado o no se almacena en
        # el arreglo de la colección (0 = fuera, 1 = dentro), que luego se mapea
        # a color azul (fuera) y rojo (dentro).
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
        canvas.widgetlock(self.lasso)  # adquirir un bloqueo en el dibujo del widget

    def on_release(self, event):
        canvas = self.collection.figure.canvas
        if hasattr(self, 'lasso') and canvas.widgetlock.isowner(self.lasso):
            canvas.widgetlock.release(self.lasso)
```
