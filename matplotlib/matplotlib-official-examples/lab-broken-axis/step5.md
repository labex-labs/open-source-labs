# Set the Y-Axis Limits

We will limit the y-axis of the first subplot to show only the outliers and the second subplot to show the majority of the data. We will use `ax1.set_ylim` and `ax2.set_ylim` to set the y-axis limits.

```python
ax1.set_ylim(.78, 1.)  # outliers only
ax2.set_ylim(0, .22)  # most of the data
```
