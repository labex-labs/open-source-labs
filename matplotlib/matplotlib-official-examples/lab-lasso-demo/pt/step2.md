# Criar a Classe LassoManager

Em seguida, crie a classe `LassoManager` que irá lidar com a funcionalidade lasso. O método `__init__` inicializa o gráfico e o objeto collection. O método `callback` altera a cor dos pontos selecionados, e os métodos `on_press` e `on_release` lidam com os eventos do mouse.

```python
class LassoManager:
    def __init__(self, ax, data):
        # A informação sobre se um ponto foi selecionado ou não é armazenada no
        # array da collection (0 = fora, 1 = dentro), que então é mapeado por cores para azul
        # (fora) e vermelho (dentro).
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
        canvas.widgetlock(self.lasso)  # acquire a lock on the widget drawing

    def on_release(self, event):
        canvas = self.collection.figure.canvas
        if hasattr(self, 'lasso') and canvas.widgetlock.isowner(self.lasso):
            canvas.widgetlock.release(self.lasso)
```
