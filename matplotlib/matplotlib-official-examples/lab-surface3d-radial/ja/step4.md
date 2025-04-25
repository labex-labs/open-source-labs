# 曲面を描画する

このステップでは、Matplotlib の `plot_surface()` 関数を使って曲面を描画します。曲面の色を設定するために、カラーマップ `YlGnBu_r` を使います。

```python
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)
```
