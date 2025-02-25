# 床にLaTeX式を書く

`text3d`関数を使用して、3Dプロットのz = 0の「床」にLaTeX式を書きます。

```python
text3d(ax, (1, 5, 0),
       r"$\displaystyle G_{\mu\nu} + \Lambda g_{\mu\nu} = "
       r"\frac{8\pi G}{c^4} T_{\mu\nu}  $",
       zdir="z", size=1, usetex=True,
       ec="none", fc="k")
```
