# 曲面を描画する

最後に、`plot_trisurf()` 関数を使って曲面を描画します。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.plot_trisurf(triang, z, cmap=plt.cm.CMRmap)
```
