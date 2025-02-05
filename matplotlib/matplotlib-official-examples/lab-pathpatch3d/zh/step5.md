# 在地面上书写一个 LaTeX 公式

我们将使用 `text3d` 函数在 3D 绘图的 z = 0“地面”上书写一个 LaTeX 公式。

```python
text3d(ax, (1, 5, 0),
       r"$\displaystyle G_{\mu\nu} + \Lambda g_{\mu\nu} = "
       r"\frac{8\pi G}{c^4} T_{\mu\nu}  $",
       zdir="z", size=1, usetex=True,
       ec="none", fc="k")
```
