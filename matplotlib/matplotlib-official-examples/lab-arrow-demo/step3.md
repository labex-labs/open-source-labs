# Customize the Arrow Graph

The third step is to customize the arrow graph. We can change the arrow property to display using the `display` parameter. We can also change the shape of the arrow using the `shape` parameter. We can adjust the width and separation of the arrows using the `max_arrow_width` and `arrow_sep` parameters, respectively. We can change the transparency of the arrows using the `alpha` parameter. We can also change the color of the label using the `labelcolor` parameter.

```python
# Plot the arrow graph with customizations
size = 4
fig = plt.figure(figsize=(3 * size, size), layout="constrained")
axs = fig.subplot_mosaic([["length", "width", "alpha"]])

for display, ax in axs.items():
    make_arrow_graph(
        ax, data, display=display, linewidth=0.001, edgecolor=None,
        normalize_data=True, size=size, shape='full', max_arrow_width=0.05,
        arrow_sep=0.03, alpha=0.7, labelcolor='white')

plt.show()
```
