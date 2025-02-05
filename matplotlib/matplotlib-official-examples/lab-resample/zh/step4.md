# 更新数据

我们将定义一个 `update` 方法来更新数据。该方法将把 ax（坐标轴）作为输入参数。我们会通过获取视图限制并检查视图限制的宽度是否与差值不同来更新线条。如果视图限制的宽度与差值不同，我们将更新差值并获取 xstart 和 xend。然后我们会将数据设置为下采样后的数据并绘制空闲状态。

```python
def update(self, ax):
    # Update the line
    lims = ax.viewLim
    if abs(lims.width - self.delta) > 1e-8:
        self.delta = lims.width
        xstart, xend = lims.intervalx
        self.line.set_data(*self.downsample(xstart, xend))
        ax.figure.canvas.draw_idle()
```
