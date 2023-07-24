# Create a Subplot

We will create a subplot to show the colored line segments. We will use the `subplots` function from `matplotlib.pyplot` to create a 2x1 grid of subplots, and the `sharex` and `sharey` parameters to share the x and y axes between the subplots.

```python
fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
line = axs[0].add_collection(lc)
fig.colorbar(line, ax=axs[0])
```
