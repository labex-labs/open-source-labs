# 自定义刻度和标签

我们将使用 `ax1.tick_params()` 方法自定义坐标轴的刻度和标签。我们将设置 x 轴标签的颜色、旋转角度和大小，以及 y 轴刻度的颜色、大小和宽度。

```python
ax1.tick_params(axis='x', labelcolor='tab:red', labelrotation=45, labelsize=16)
ax1.tick_params(axis='y', color='tab:green', size=25, width=3)
```
