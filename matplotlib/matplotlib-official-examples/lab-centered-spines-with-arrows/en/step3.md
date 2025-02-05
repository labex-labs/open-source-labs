# Move the spines

By default, the spines are drawn at the edges of the plot. In this case, you want to move the left and bottom spines to the center of the plot.

```python
ax.spines[["left", "bottom"]].set_position(("data", 0))
```
