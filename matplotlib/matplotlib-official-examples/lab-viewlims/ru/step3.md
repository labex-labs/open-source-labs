# Создаем класс MandelbrotDisplay

Мы создадим класс под названием MandelbrotDisplay, который будет перегенерировать фрактальное множество при приближении, чтобы мы могли на самом деле увидеть увеличивающуюся деталь. Коробка на левой панели покажет область, на которую мы приближаемся.

```python
class MandelbrotDisplay:
    def __init__(self, h=500, w=500, niter=50, radius=2., power=2):
        self.height = h
        self.width = w
        self.niter = niter
        self.radius = radius
        self.power = power

    def compute_image(self, xstart, xend, ystart, yend):
        self.x = np.linspace(xstart, xend, self.width)
        self.y = np.linspace(ystart, yend, self.height).reshape(-1, 1)
        c = self.x + 1.0j * self.y
        threshold_time = np.zeros((self.height, self.width))
        z = np.zeros(threshold_time.shape, dtype=complex)
        mask = np.ones(threshold_time.shape, dtype=bool)
        for i in range(self.niter):
            z[mask] = z[mask]**self.power + c[mask]
            mask = (np.abs(z) < self.radius)
            threshold_time += mask
        return threshold_time

    def ax_update(self, ax):
        ax.set_autoscale_on(False)
        self.width, self.height = \
            np.round(ax.patch.get_window_extent().size).astype(int)
        vl = ax.viewLim
        extent = vl.x0, vl.x1, vl.y0, vl.y1
        im = ax.images[-1]
        im.set_data(self.compute_image(*extent))
        im.set_extent(extent)
        ax.figure.canvas.draw_idle()
```
