# Define Add Floating Axis Function

Define the `add_floating_axis` function, which adds a floating axis to the plot. This function takes in the `ax1` object as an argument and returns the `axis` object.

```python
def add_floating_axis(ax1):
    # Define the floating axis
    ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 30)
    axis.label.set_text(r"$\theta = 30^{\circ}$")
    axis.label.set_visible(True)

    return axis
```
