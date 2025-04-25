# 配置坐标轴样式

现在，我们将通过在每个坐标轴的末端添加箭头，并从原点添加 X 轴和 Y 轴来配置坐标轴样式。

```python
for direction in ["xzero", "yzero"]:
    # 在每个坐标轴的末端添加箭头
    ax.axis[direction].set_axisline_style("-|>")
    # 从原点添加 X 轴和 Y 轴
    ax.axis[direction].set_visible(True)

# 隐藏边框
for direction in ["left", "right", "bottom", "top"]:
    ax.axis[direction].set_visible(False)
```
