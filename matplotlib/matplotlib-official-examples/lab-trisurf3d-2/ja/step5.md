# 曲面を描画する

最後に、`plot_trisurf()` 関数を使って曲面を描画します。パラメータ空間の三角形が、どの `x`、`y`、`z` の点が辺で接続されているかを決定します。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(x, y, z, triangles=tri.triangles, cmap=plt.cm.Spectral)
ax.set_zlim(-1, 1)
```
