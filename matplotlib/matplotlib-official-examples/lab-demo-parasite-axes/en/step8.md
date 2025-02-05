# Add legend and axis colors

We add a legend to the host axes using `host.legend()` method. We also set the color of the left y-axis label of the host axes, the right y-axis label of the first parasite axes, and the right y-axis label of the second parasite axes to match their respective lines using `host.axis["left"].label.set_color(p1.get_color())`, `par1.axis["right"].label.set_color(p2.get_color())`, and `par2.axis["right2"].label.set_color(p3.get_color())` methods.

```python
host.legend()

host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())
```
