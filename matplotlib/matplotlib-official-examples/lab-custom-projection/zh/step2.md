# 创建 GeoAxes 类

我们将创建一个名为 `GeoAxes` 的地理投影抽象基类。

```python
class GeoAxes(Axes):
    """
    地理投影的抽象基类
    """

    class ThetaFormatter(Formatter):
        """
        用于格式化 theta 刻度标签。将弧度的原生单位转换为度并添加度符号。
        """
        def __init__(self, round_to=1.0):
            self._round_to = round_to

        def __call__(self, x, pos=None):
            degrees = round(np.rad2deg(x) / self._round_to) * self._round_to
            return f"{degrees:0.0f}\N{DEGREE SIGN}"

    RESOLUTION = 75

    def _init_axis(self):
        self.xaxis = maxis.XAxis(self)
        self.yaxis = maxis.YAxis(self)
        # 在 GeoAxes.xaxis.clear() 正常工作之前，不要像在 Axes._init_axis() 中那样将 xaxis 或 yaxis 注册到脊柱（spines）上。
        # self.spines['geo'].register_axis(self.yaxis)

    def clear(self):
        # 继承的文档字符串
        super().clear()

        self.set_longitude_grid(30)
        self.set_latitude_grid(15)
        self.set_longitude_grid_ends(75)
        self.xaxis.set_minor_locator(NullLocator())
        self.yaxis.set_minor_locator(NullLocator())
        self.xaxis.set_ticks_position('none')
        self.yaxis.set_ticks_position('none')
        self.yaxis.set_tick_params(label1On=True)
        # 为什么我们需要打开 y 轴刻度标签，而 x 轴刻度标签已经打开了呢？

        self.grid(rcParams['axes.grid'])

        Axes.set_xlim(self, -np.pi, np.pi)
        Axes.set_ylim(self, -np.pi / 2.0, np.pi / 2.0)
```
