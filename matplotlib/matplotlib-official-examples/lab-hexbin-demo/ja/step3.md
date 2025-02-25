# 六角形のビン付きプロットを作成する

`matplotlib.pyplot.hexbin()` を使って六角形のビン付きプロットを作成します。

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("Hexagon binning")

cb = fig.colorbar(hb, ax=ax, label='counts')
```

ここでは、グリッドサイズを 50 に設定し、カラーマップを 'inferno' に設定しています。また、各六角形内のデータポイントの数を示すカラーバーを追加しています。
