# 壁に円を描画する

Matplotlibの`Circle`と`pathpatch_2d_to_3d`関数を使用して、3Dプロットのx = 0の「壁」に円を描画します。

```python
p = Circle((5, 5), 3)
ax.add_patch(p)
art3d.pathpatch_2d_to_3d(p, z=0, zdir="x")
```
