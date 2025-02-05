# 为底部和左侧自定义脊柱（坐标轴框架）

在第二个子图中，我们将仅在绘图的底部和左侧显示脊柱（坐标轴框架）。我们可以使用`set_visible`方法隐藏绘图右侧和顶部的脊柱（坐标轴框架）。

```python
ax1.plot(x, y)
ax1.set_title('Bottom-Left Spines')

# Hide the right and top spines
ax1.spines.right.set_visible(False)
ax1.spines.top.set_visible(False)
```
