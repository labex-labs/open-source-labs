# Make X Axis Line Visible at Y=0

We will now make the x axis line visible at y=0. This is done by setting the xzero axis to visible.

```python
ax.axis["xzero"].set_visible(True)
ax.axis["xzero"].label.set_text("Axis Zero")
```
