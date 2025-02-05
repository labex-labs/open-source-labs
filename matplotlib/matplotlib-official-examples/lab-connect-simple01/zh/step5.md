# 在不同点之间绘制一条线

最后，让我们在不同坐标系中定义的不同点之间绘制一条线。

```python
con = ConnectionPatch(
    # 在轴坐标中
    xyA=(0.6, 1.0), coordsA=ax2.transAxes,
    # x 在轴坐标中，y 在数据坐标中
    xyB=(0.0, 0.2), coordsB=ax2.get_yaxis_transform(),
    arrowstyle="-")
ax2.add_artist(con)
```
