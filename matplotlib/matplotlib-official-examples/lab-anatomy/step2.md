# Create the figure and set up the axes

Next, we will create a figure and set up the axes. We will use the `add_axes()` method to create a new set of axes within the figure. We will also set limits for the x and y axes and add gridlines.

```python
# Create figure and axes
fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_axes([0.2, 0.17, 0.68, 0.7], aspect=1)

# Set limits and gridlines
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)
ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=-10)
```
