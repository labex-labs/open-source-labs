# Adding Floating Axis

We will define two functions that will add floating axes to our plot. The first function `add_floating_axis1()` adds a floating axis to the plot with a label of `theta = 30`. The second function `add_floating_axis2()` adds a floating axis to the plot with a label of `r = 6`.

```python
def add_floating_axis1(ax):
    ax.axis["lat"] = axis = ax.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)
    return axis

def add_floating_axis2(ax):
    ax.axis["lon"] = axis = ax.new_floating_axis(1, 6)
    axis.label.set_text(r"$r = 6$")
    axis.label.set_visible(True)
    return axis
```
