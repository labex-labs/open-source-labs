# Создание класса PathInteractor

В этом шаге мы создаем класс PathInteractor, который обрабатывает вызовы обратных функций для объекта пути. Этот класс позволяет нам интерактивно редактировать путь, перетаскивая маркеры на графике.

```python
class PathInteractor:
    """
    Редактор пути.

    Нажмите 't', чтобы переключить маркеры вершин вкл/выкл. Когда маркеры вершин включены,
    их можно перетаскивать мышью.
    """

    showverts = True
    epsilon = 5  # максимальное расстояние в пикселях, при котором точка считается попавшей в вершину

    def __init__(self, pathpatch):

        self.ax = pathpatch.axes
        canvas = self.ax.figure.canvas
        self.pathpatch = pathpatch
        self.pathpatch.set_animated(True)

        x, y = zip(*self.pathpatch.get_path().vertices)

        self.line, = ax.plot(
            x, y, marker='o', markerfacecolor='r', animated=True)

        self._ind = None  # активная вершина

        canvas.mpl_connect('draw_event', self.on_draw)
        canvas.mpl_connect('button_press_event', self.on_button_press)
        canvas.mpl_connect('key_press_event', self.on_key_press)
        canvas.mpl_connect('button_release_event', self.on_button_release)
        canvas.mpl_connect('motion_notify_event', self.on_mouse_move)
        self.canvas = canvas

    def get_ind_under_point(self, event):
        """
        Возвращает индекс точки, ближайшей к позиции события, или *None*,
        если нет точки в пределах ``self.epsilon`` от позиции события.
        """
        xy = self.pathpatch.get_path().vertices
        xyt = self.pathpatch.get_transform().transform(xy)  # в координаты отображения
        xt, yt = xyt[:, 0], xyt[:, 1]
        d = np.sqrt((xt - event.x)**2 + (yt - event.y)**2)
        ind = d.argmin()
        return ind if d[ind] < self.epsilon else None

    def on_draw(self, event):
        """Обратный вызов для отрисовок."""
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.pathpatch)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)

    def on_button_press(self, event):
        """Обратный вызов для нажатий кнопок мыши."""
        if (event.inaxes is None
                or event.button!= MouseButton.LEFT
                or not self.showverts):
            return
        self._ind = self.get_ind_under_point(event)

    def on_button_release(self, event):
        """Обратный вызов для отпусканий кнопок мыши."""
        if (event.button!= MouseButton.LEFT
                or not self.showverts):
            return
        self._ind = None

    def on_key_press(self, event):
        """Обратный вызов для нажатий клавиш."""
        if not event.inaxes:
            return
        if event.key == 't':
            self.showverts = not self.showverts
            self.line.set_visible(self.showverts)
            if not self.showverts:
                self._ind = None
        self.canvas.draw()

    def on_mouse_move(self, event):
        """Обратный вызов для движений мыши."""
        if (self._ind is None
                or event.inaxes is None
                or event.button!= MouseButton.LEFT
                or not self.showverts):
            return

        vertices = self.pathpatch.get_path().vertices

        vertices[self._ind] = event.xdata, event.ydata
        self.line.set_data(zip(*vertices))

        self.canvas.restore_region(self.background)
        self.ax.draw_artist(self.pathpatch)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)
```
