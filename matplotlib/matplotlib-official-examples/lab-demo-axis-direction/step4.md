# Changing the Axis Direction

Now, we will create a loop to set up four different plots with the floating axis in each of the four cardinal directions. In the loop, we will use `add_floating_axis1()` and `add_floating_axis2()` to add the floating axes, and `set_axis_direction()` to set the axis direction.

```python
fig = plt.figure(figsize=(8, 4), layout="constrained")

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=241+i)
    axis = add_floating_axis1(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

for i, d in enumerate(["bottom", "left", "top", "right"]):
    ax = setup_axes(fig, rect=245+i)
    axis = add_floating_axis2(ax)
    axis.set_axis_direction(d)
    ax.set(title=d)

plt.show()
```
