# Create a function to set up axes

We will create a function to set up our axes with the desired tick labels.

```python
def setup_axes(fig, pos):
    ax = fig.add_subplot(pos, axes_class=axislines.Axes)
    ax.set_yticks([0.2, 0.8])
    ax.set_xticks([0.2, 0.8])
    return ax
```
