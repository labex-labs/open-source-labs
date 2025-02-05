# 在墙上绘制一个圆

我们将使用 Matplotlib 的 `Circle` 和 `pathpatch_2d_to_3d` 函数在 3D 绘图的 x = 0“墙”上绘制一个圆。

```python
p = Circle((5, 5), 3)
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")
```
