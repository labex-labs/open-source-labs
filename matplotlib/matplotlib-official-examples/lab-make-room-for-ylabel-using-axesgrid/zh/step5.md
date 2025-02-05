# 为 y 轴标签留出空间并调整坐标轴

在这一步中，我们使用 `make_axes_area_auto_adjustable` 方法为两个坐标轴中的 y 轴标签留出空间。我们还使用 `use_axes` 参数指定要调整的坐标轴，并使用 `pad` 参数调整坐标轴之间的间距。

```python
make_axes_area_auto_adjustable(ax1, pad=0.1, use_axes=[ax1, ax2])
make_axes_area_auto_adjustable(ax2, pad=0.1, use_axes=[ax1, ax2])
```
