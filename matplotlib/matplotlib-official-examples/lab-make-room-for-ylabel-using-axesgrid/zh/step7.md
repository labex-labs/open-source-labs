# 调整坐标轴并为 y 轴标签留出空间

在这一步中，我们使用 `add_auto_adjustable_area` 方法来调整坐标轴并为 y 轴标签留出空间。我们还为第二个坐标轴设置标题和 x 轴标签。

```python
divider.add_auto_adjustable_area(use_axes=[ax1], pad=0.1,
                                 adjust_dirs=["left"])
divider.add_auto_adjustable_area(use_axes=[ax2], pad=0.1,
                                 adjust_dirs=["right"])
divider.add_auto_adjustable_area(use_axes=[ax1, ax2], pad=0.1,
                                 adjust_dirs=["top", "bottom"])

ax1.set_yticks([0.5], labels=["非常长的标签"])
ax2.set_title("标题")
ax2.set_xlabel("X - 标签")
```
