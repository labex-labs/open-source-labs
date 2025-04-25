# 为中心子图添加标签

我们为中心子图添加一个标签，以表明这是一个主要的 3D 视图平面绘图。

```python
label ='mplot3d primary view planes\n' + 'ax.view_init(elev, azim, roll)'
annotate_axes(axd['L'], label, fontsize=18)
axd['L'].set_axis_off()
```
