# Set the Axis Labels

We set the axis labels for the left and right sides of the plot using the `ax1.axis[]` function. We also set the direction of the tick labels using the `set_axis_direction()` function.

```python
ax1.axis["left"].major_ticklabels.set_axis_direction("top")
ax1.axis["left"].label.set_text("Left label")

ax1.axis["right"].label.set_visible(True)
ax1.axis["right"].label.set_text("Right label")
ax1.axis["right"].label.set_axis_direction("left")
```
