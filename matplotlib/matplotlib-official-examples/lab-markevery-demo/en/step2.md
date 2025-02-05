# Create Plots with Linear Scales

Next, we create a set of subplots to show how `markevery` behaves with linear scales. We iterate through the `cases` list and plot each case on a separate subplot. We use the `markevery` parameter to specify which data points to mark.

```python
# create plots with linear scales
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
