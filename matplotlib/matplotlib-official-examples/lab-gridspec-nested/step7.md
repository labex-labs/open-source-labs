# Format the Axes

We will format the axes of all the subplots using the `format_axes` function. This function will add a text label to each subplot and remove the tick labels.

```python
def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.tick_params(labelbottom=False, labelleft=False)

format_axes(fig)
```
