# 隐藏坐标轴边框

现在，我们将使用 `ax1.spines.bottom.set_visible` 和 `ax2.spines.top.set_visible` 隐藏两个子图之间的坐标轴边框。

```python
ax1.spines.bottom.set_visible(False)
ax2.spines.top.set_visible(False)
```
