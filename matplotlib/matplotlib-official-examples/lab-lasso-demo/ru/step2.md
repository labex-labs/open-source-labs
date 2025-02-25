# Создать класс LassoManager

Далее создадим класс `LassoManager`, который будет обрабатывать функциональность лассо. Метод `__init__` инициализирует объект графика и коллекцию. Метод `callback` изменяет цвет выбранных точек, а методы `on_press` и `on_release` обрабатывают события мыши.

```python
class LassoManager:
    def __init__(self, ax, data):
        # Информация о том, была ли точка выбрана или нет, хранится в массиве коллекции (0 = вне, 1 = внутри),
        # который затем отображается с помощью цветовой карты в синий (вне) и красный (внутри).
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
        canvas.widgetlock(self.lasso)  # получить блокировку для рисования виджета

    def on_release(self, event):
        canvas = self.collection.figure.canvas
        if hasattr(self, 'lasso') and canvas.widgetlock.isowner(self.lasso):
            canvas.widgetlock.release(self.lasso)
```
