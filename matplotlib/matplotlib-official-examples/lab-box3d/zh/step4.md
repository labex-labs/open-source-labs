# 设置绘图范围

使用 `set` 方法并传入 X、Y 和 Z 坐标的范围来设置绘图范围。

```python
# 根据坐标范围设置绘图范围
xmin, xmax = X.min(), X.max()
ymin, ymax = Y.min(), Y.max()
zmin, zmax = Z.min(), Z.max()
ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax], zlim=[zmin, zmax])
```
