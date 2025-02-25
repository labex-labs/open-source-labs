# プロットの範囲を設定する

`set` メソッドを使って、X、Y、Z 座標の範囲を指定して、プロットの範囲を設定します。

```python
# Set limits of the plot from coord limits
xmin, xmax = X.min(), X.max()
ymin, ymax = Y.min(), Y.max()
zmin, zmax = Z.min(), Z.max()
ax.set(xlim=[xmin, xmax], ylim=[ymin, ymax], zlim=[zmin, zmax])
```
