# 创建范围滑块

现在我们将创建范围滑块（RangeSlider）小部件，它将允许我们调整图像的阈值。我们将为滑块创建一个新的轴，并将其添加到图形中。

```python
slider_ax = fig.add_axes([0.20, 0.1, 0.60, 0.03])
slider = RangeSlider(slider_ax, "Threshold", img.min(), img.max())
```
