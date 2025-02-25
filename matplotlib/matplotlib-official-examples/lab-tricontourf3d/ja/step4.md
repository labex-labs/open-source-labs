# グラフの作成

ここで、`tricontourf()` 関数を使ってグラフを作成し、視点をカスタマイズします。

```python
ax = plt.figure().add_subplot(projection='3d')
ax.tricontourf(triang, z, cmap=plt.cm.CMRmap)
ax.view_init(elev=45.)

plt.show()
```
