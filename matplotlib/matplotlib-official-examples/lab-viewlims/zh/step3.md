# 创建 MandelbrotDisplay 类

我们将创建一个名为 MandelbrotDisplay 的类，它会在我们放大时重新生成一个分形集，以便我们能够实际看到不断增加的细节。左侧面板中的一个框将显示我们所放大的区域。

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
