# Create Floating Axes

In this step, we will create two floating axes that will be used to display the polar curve in a rectangular box. We will use `new_floating_axis()` to create the floating axes.

```python
# Create the floating axes
ax1.axis["lat"] = axis = ax1.new_floating_axis(0, 60)
axis.label.set_text(r"$\theta = 60^{\circ}$")
axis.label.set_visible(True)

ax1.axis["lon"] = axis = ax1.new_floating_axis(1, 6)
axis.label.set_text(r"$r = 6$")
```
