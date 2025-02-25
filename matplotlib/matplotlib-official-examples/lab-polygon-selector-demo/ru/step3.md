# Определение класса селектора

В этом шаге мы определим класс, который позволит нам выбирать точки из точечного графика с использованием инструмента "Выбор полигоном". Этот класс сохранит индексы выбранных точек в массиве.

```python
class SelectFromCollection:
    """
    Выбирает индексы из коллекции matplotlib с использованием `PolygonSelector`.

    Выбранные индексы сохраняются в атрибуте `ind`. Этот инструмент делает менее заметными точки, которые не входят в выбор (то есть уменьшает их значения альфа). Если у вашей коллекции альфа < 1, этот инструмент будет постоянно изменять значения альфа.

    Обратите внимание, что этот инструмент выбирает объекты коллекции на основе их *исходных точек* (то есть `offsets`).

    Параметры
    ----------
    ax : `~matplotlib.axes.Axes`
        Окно для взаимодействия.
    collection : `matplotlib.collections.Collection` подкласс
        Коллекция, из которой вы хотите выбирать.
    alpha_other : 0 <= float <= 1
        Чтобы выделить выбор, этот инструмент устанавливает все выбранные точки с альфа значением 1, а невыбранные точки - с значением *alpha_other*.
    """

    def __init__(self, ax, collection, alpha_other=0.3):
        self.canvas = ax.figure.canvas
        self.collection = collection
        self.alpha_other = alpha_other

        self.xys = collection.get_offsets()
        self.Npts = len(self.xys)

        # Убедитесь, что у каждого объекта есть отдельные цвета
        self.fc = collection.get_facecolors()
        if len(self.fc) == 0:
            raise ValueError('Коллекция должна иметь цвет для лица')
        elif len(self.fc) == 1:
            self.fc = np.tile(self.fc, (self.Npts, 1))

        self.poly = PolygonSelector(ax, self.onselect, draw_bounding_box=True)
        self.ind = []

    def onselect(self, verts):
        path = Path(verts)
        self.ind = np.nonzero(path.contains_points(self.xys))[0]
        self.fc[:, -1] = self.alpha_other
        self.fc[self.ind, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()

    def disconnect(self):
        self.poly.disconnect_events()
        self.fc[:, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()
```
