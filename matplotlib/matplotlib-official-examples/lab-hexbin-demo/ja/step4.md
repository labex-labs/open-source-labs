# 対数カラースケールを追加する

`hexbin()` の `bins='log'` を設定することで、六角形のビン付きプロットに対数カラースケールを追加することができます。

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, bins='log', cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("With a log color scale")

cb = fig.colorbar(hb, ax=ax, label='log10(N)')
```
