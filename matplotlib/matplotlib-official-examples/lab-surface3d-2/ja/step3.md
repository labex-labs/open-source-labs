# 3D 曲面グラフの作成

これで 3D 曲面グラフを作成できます。まず、`projection='3d'` 引数を使って図を作成し、サブプロットを追加します。そして、前のステップで作成したデータを使って `plot_surface()` 関数を使って曲面を描画します。

```python
# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(x, y, z)
```
