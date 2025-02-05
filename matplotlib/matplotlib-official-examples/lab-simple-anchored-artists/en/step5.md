# Add a Size Bar

Draw a horizontal bar with a length of 0.1 in data coordinates, with a fixed label underneath.

```python
asb = AnchoredSizeBar(ax.transData,
                      0.1,
                      r"1$^{\prime}$",
                      loc='lower center',
                      pad=0.1, borderpad=0.5, sep=5,
                      frameon=False)
ax.add_artist(asb)
```
