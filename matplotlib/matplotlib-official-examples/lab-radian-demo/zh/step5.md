# 在第二个子图中绘制数据

使用 matplotlib.pyplot 中的 plot 函数，在第二个子图中绘制 x 值的余弦值。使用 xunits 参数指定 x 轴应以度为单位。

```python
from basic_units import degrees
axs[1].plot(x, cos(x), xunits=degrees)
```
