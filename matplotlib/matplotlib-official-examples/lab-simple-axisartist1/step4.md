# Create Subplot 2

In the second subplot, we will use `axisartist.axislines.AxesZero` to automatically create xzero and yzero axes. We will make the other spines invisible and set the xzero axis visible.

```python
ax1 = fig.add_subplot(gs[0, 1], axes_class=axisartist.axislines.AxesZero)
ax1.axis["xzero"].set_visible(True)
ax1.axis["xzero"].label.set_text("Axis Zero")
ax1.axis["bottom", "top", "right"].set_visible(False)
```
