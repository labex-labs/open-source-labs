# Создать класс селектора

Создайте класс `SelectFromCollection`, который будет выбирать индексы из коллекции Matplotlib с использованием `LassoSelector`.

```python
class SelectFromCollection:
    """
    Выбирает индексы из коллекции matplotlib с использованием `LassoSelector`.

    Выбранные индексы сохраняются в атрибуте `ind`. Эта工具 делает непрозрачными точки, которые не входят в выбор (то есть, уменьшает их значения альфа). Если у вашей коллекции альфа < 1, эта工具 будет постоянно изменять значения альфа.

    Обратите внимание, что эта工具 выбирает объекты коллекции на основе их *исходных точек* (то есть, `offsets`).

    Параметры
    ----------
    ax : `~matplotlib.axes.Axes`
        оси для взаимодействия.
    collection : `matplotlib.collections.Collection` подкласс
        коллекция, из которой вы хотите выбрать.
    alpha_other : 0 <= float <= 1
        Чтобы выделить выбор, эта工具 устанавливает все выбранные точки в значение альфа 1, а невыбранные точки в *alpha_other*.
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
            raise ValueError('Коллекция должна иметь цвет лица')
        elif len(self.fc) == 1:
            self.fc = np.tile(self.fc, (self.Npts, 1))

        self.lasso = LassoSelector(ax, onselect=self.onselect)
        self.ind = []

    def onselect(self, verts):
        path = Path(verts)
        self.ind = np.nonzero(path.contains_points(self.xys))[0]
        self.fc[:, -1] = self.alpha_other
        self.fc[self.ind, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()

    def disconnect(self):
        self.lasso.disconnect_events()
        self.fc[:, -1] = 1
        self.collection.set_facecolors(self.fc)
        self.canvas.draw_idle()
```
