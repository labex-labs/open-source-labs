# データの作成

このステップでは、可視化するためのいくつかのデータを作成します。グリッド上の点の散布図を作成します。

```python
fig, ax = plt.subplots()
grid_size = 5
grid_x = np.tile(np.arange(grid_size), grid_size)
grid_y = np.repeat(np.arange(grid_size), grid_size)
pts = ax.scatter(grid_x, grid_y)
```
