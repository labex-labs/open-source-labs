# Create Plots with Logarithmic Scales

We repeat the previous step, but this time with logarithmic scales. We note that the logarithmic scale causes a visual asymmetry in the marker distance for integer-based subsampling, while fraction-based subsampling creates even distributions.

```python
# create plots with logarithmic scales
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
