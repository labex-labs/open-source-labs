# Hide Top and Right Axes

We will now hide the top and right axes, since we only need the left and bottom axes.

```python
ax.axis["right"].set_visible(False)
ax.axis["top"].set_visible(False)
```
