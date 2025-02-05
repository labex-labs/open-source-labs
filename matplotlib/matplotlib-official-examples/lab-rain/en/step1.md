# Create a new Figure and Axes

The first step is to create a new figure and an axes which fills it. This will be the canvas on which the simulation will be drawn.

```python
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])
```
