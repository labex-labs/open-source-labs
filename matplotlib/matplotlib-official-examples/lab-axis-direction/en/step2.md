# Create a Function to Set Up Axes

We will create a function called `setup_axes` to set up the axes for our plots. This function takes in two parameters, a `fig` object and a `pos` object. The `fig` object is the figure object that we will be plotting on, and the `pos` object is the position of the subplot within the figure.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axisartist.Axes)

    ax.set_ylim(-0.1, 1.5)
    ax.set_yticks([0, 1])

    ax.axis[:].set_visible(False)

    ax.axis["x"] = ax.new_floating_axis(1, 0.5)
    ax.axis["x"].set_axisline_style("->", size=1.5)

    return ax
```
