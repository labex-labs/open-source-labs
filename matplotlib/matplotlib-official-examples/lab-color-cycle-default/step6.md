# Customize subplots

We customize the subplots by setting the background color of the bottom subplots to black, setting the x-axis ticks, and adding a title to each subplot.

```python
axs[1, icol].set_facecolor('k')
axs[1, icol].xaxis.set_ticks(np.arange(0, 10, 2))
axs[0, icol].set_title(f'line widths (pts): {lwx:g}, {lwy:g}',
                       fontsize='medium')
```
