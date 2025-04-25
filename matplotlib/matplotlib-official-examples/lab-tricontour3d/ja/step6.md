# 3D コンター図を作成する

作成した三角分割と z 座標を使って 3D コンター図を作成します。また、プロットを理解しやすくするために視点をカスタマイズします。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontour(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)
plt.show()
```
