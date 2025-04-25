# 3D のステムプロットを作成する

このステップでは、Matplotlib の`stem`関数を使って 3D のステムプロットを作成します。`stem`関数に x 座標、y 座標、z 座標を引数として渡します。

```python
fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.stem(x, y, z)

plt.show()
```
