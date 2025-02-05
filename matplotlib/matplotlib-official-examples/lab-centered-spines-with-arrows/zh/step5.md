# 在脊柱线末端绘制箭头

为了指示坐标轴的方向，你可以在脊柱线的末端绘制箭头。

```python
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
```
