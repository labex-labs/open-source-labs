# Setting Limits and Removing Ticks

In this step, we will set the y limit and remove the ticks from the plot.

```python
# Set y limit (or first line is cropped because of thickness)
ax.set_ylim(-1, 70)

# No ticks
ax.set_xticks([])
ax.set_yticks([])
```
