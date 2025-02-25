# Fügen Sie eine logarithmische Farbskala hinzu

Wir können einer logarithmischen Farbskala zum hexagonalen Binned-Plot hinzufügen, indem wir `bins='log'` in `hexbin()` festlegen.

```python
fig, ax = plt.subplots(figsize=(9, 4))

hb = ax.hexbin(x, y, gridsize=50, bins='log', cmap='inferno')
ax.set(xlim=xlim, ylim=ylim)
ax.set_title("With a log color scale")

cb = fig.colorbar(hb, ax=ax, label='log10(N)')
```
