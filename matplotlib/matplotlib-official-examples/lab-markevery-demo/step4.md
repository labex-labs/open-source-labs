# Create Zoomed Plots

We create another set of subplots, this time to show how `markevery` behaves on zoomed plots. We note that integer-based subsampling selects points from the underlying data and is independent of the view, while float-based subsampling is related to the Axes diagonal and changes the displayed data range.

```python
# create zoomed plots
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
    ax.set_xlim((6, 6.7))
    ax.set_ylim((1.1, 1.7))
```
