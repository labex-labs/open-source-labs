# Create the plot and connect the scroll event

We will create the plot using Matplotlib's `subplots` function and pass the created `IndexTracker` object to it. Then, we will connect the scroll event to the figure canvas using `mpl_connect`.

```python
fig, ax = plt.subplots()
tracker = IndexTracker(ax, X)

fig.canvas.mpl_connect('scroll_event', tracker.on_scroll)
plt.show()
```
