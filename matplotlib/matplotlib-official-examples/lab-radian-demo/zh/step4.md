# 在第一个子图中绘制数据

使用 matplotlib.pyplot 中的 plot 函数，在第一个子图中绘制 x 值的余弦值。使用 xunits 参数指定 x 轴应以弧度为单位。

```python
from basic_units import cos
axs[0].plot(x, cos(x), xunits=radians)
```
