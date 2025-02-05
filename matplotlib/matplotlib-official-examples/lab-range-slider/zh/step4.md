# 在直方图中添加垂直线

为了更便于观察阈值处理的效果，我们将在直方图中添加垂直线，以指示当前的阈值。我们将分别为下限和上限阈值创建两条线。

```python
lower_limit_line = axs[1].axvline(slider.val[0], color='k')
upper_limit_line = axs[1].axvline(slider.val[1], color='k')
```
