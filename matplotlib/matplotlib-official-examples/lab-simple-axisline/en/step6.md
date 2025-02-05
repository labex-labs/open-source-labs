# Create Y2 Axis

Finally, we will create a new y2 axis on the right side of the plot with an offset of (20, 0) and label it.

```python
ax.axis["right2"] = ax.new_fixed_axis(loc="right", offset=(20, 0))
ax.axis["right2"].label.set_text("Label Y2")
```
