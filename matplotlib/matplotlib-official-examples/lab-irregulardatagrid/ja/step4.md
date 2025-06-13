# Tricontour (トライコントゥア)

`axes.Axes.tricontour` に順序付けられていない、不規則に配置された座標を直接供給することにより、同じデータを tricontour プロットを使用してプロットします。

```python
fig, ax2 = plt.subplots()
cntr2 = ax2.tricontourf(x, y, z, levels=14, cmap="RdBu_r")
ax2.plot(x, y, 'ko', ms=3)
ax2.set(xlim=(-2, 2), ylim=(-2, 2))
ax2.set_title('Tricontour Plot of Irregularly Spaced Data')
fig.colorbar(cntr2, ax=ax2)
plt.show()
```
