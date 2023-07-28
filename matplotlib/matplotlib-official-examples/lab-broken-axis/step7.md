# Adjust the Ticks

We will now adjust the ticks on the x-axis. We will move the ticks on the first subplot to the top using `ax1.xaxis.tick_top`, remove the tick labels on the first subplot using `ax1.tick_params(labeltop=False)`, and keep the tick labels on the second subplot.

```python
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)
ax2.xaxis.tick_bottom()
```
