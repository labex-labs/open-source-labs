# グリッド上の補間

グリッド上での補間を通じて、不規則な間隔のデータ座標のコンター図を作成します。まず、`np.linspace` を使って x と y のグリッド値を作成します。次に、`tri.LinearTriInterpolator` を使って、(xi, yi) によって定義されるグリッド上でデータ (x, y) を線形補間します。通常の `axes.Axes.contour` を使って補間されたデータをプロットします。

```python
ngridx = 100
ngridy = 200
xi = np.linspace(-2.1, 2.1, ngridx)
yi = np.linspace(-2.1, 2.1, ngridy)

triang = tri.Triangulation(x, y)
interpolator = tri.LinearTriInterpolator(triang, z)
Xi, Yi = np.meshgrid(xi, yi)
zi = interpolator(Xi, Yi)

fig, ax1 = plt.subplots()
cntr1 = ax1.contourf(xi, yi, zi, levels=14, cmap="RdBu_r")
ax1.plot(x, y, 'ko', ms=3)
ax1.set(xlim=(-2, 2), ylim=(-2, 2))
ax1.set_title('Contour Plot of Irregularly Spaced Data Interpolated on a Grid')
fig.colorbar(cntr1, ax=ax1)
plt.show()
```
