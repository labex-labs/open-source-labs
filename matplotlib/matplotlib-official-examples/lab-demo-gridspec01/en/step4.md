# Annotate Axes

To annotate the axes, we can loop through the figure axes and add text using the `text` function and the `tick_params` function to remove the tick labels.

```python
def annotate_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)
```
