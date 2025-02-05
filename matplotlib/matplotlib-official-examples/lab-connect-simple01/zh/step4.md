# 在不同轴之间绘制箭头

让我们在数据坐标中的同一点之间绘制一个箭头，但在不同的轴上。

```python
xy = (0.3, 0.2)
con = ConnectionPatch(
    xyA=xy, coordsA=ax2.transData,
    xyB=xy, coordsB=ax1.transData,
    arrowstyle="->", shrinkB=5)
fig.add_artist(con)
```
