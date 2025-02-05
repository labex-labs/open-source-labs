# 隐藏顶部和右侧坐标轴

由于我们只需要左侧和底部坐标轴，现在我们将隐藏顶部和右侧坐标轴。

```python
ax.axis["right"].set_visible(False)
ax.axis["top"].set_visible(False)
```
