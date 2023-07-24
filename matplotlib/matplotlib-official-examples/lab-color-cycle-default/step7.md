# Customize y-axis ticks

We customize the y-axis ticks for the leftmost subplots.

```python
for irow in range(2):
    axs[irow, 0].yaxis.set_ticks(np.arange(0, 10, 2))
```
