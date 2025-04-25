# 三角分割、等電位線およびベクトル場を描画する

```python
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.use_sticky_edges = False
ax.margins(0.07)

ax.triplot(triang, color='0.8')

levels = np.arange(0., 1., 0.01)
ax.tricontour(tri_refi, z_test_refi, levels=levels, cmap='hot',
              linewidths=[2.0, 1.0, 1.0, 1.0])

ax.quiver(triang.x, triang.y, Ex/E_norm, Ey/E_norm,
          units='xy', scale=10., zorder=3, color='blue',
          width=0.007, headwidth=3., headlength=4.)

ax.set_title('Gradient Plot: Electrical Dipole')
plt.show()
```

解説：

- `fig`と`ax`はそれぞれグラフと軸のオブジェクトです。
- `ax.set_aspect`は軸のアスペクト比を設定します。
- `ax.use_sticky_edges`と`ax.margins`は軸の余白を設定します。
- `ax.triplot`は三角分割を描画します。
- `ax.tricontour`は等電位線を描画します。
- `ax.quiver`はベクトル場を描画します。
- `ax.set_title`はグラフのタイトルを設定します。
