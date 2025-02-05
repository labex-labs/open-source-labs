# 移动脊柱线

默认情况下，脊柱线绘制在图表的边缘。在这种情况下，你要将左侧和底部的脊柱线移动到图表的中心。

```python
ax.spines[["left", "bottom"]].set_position(("data", 0))
```
