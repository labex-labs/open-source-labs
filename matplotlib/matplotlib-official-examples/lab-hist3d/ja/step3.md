# ヒストグラムの作成

データが用意できたので、3 次元ヒストグラムを作成できます。NumPy の `histogram2d()` 関数を使ってデータの 2 次元ヒストグラムを作成し、その後 Matplotlib の `bar3d()` 関数を使ってヒストグラムの 3 次元棒グラフを作成します。

```python
hist, xedges, yedges = np.histogram2d(x, y, bins=4, range=[[0, 4], [0, 4]])

# Construct arrays for the anchor positions of the 16 bars.
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the 16 bars.
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
```
