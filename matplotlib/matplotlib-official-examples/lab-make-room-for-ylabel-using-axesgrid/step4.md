# Create a Figure with Two Axes

In this step, we create a figure with two axes. We use the `add_axes` method to add two axes to the figure. We also set the y-tick label for the first axis and the title for the second axis.

```python
fig = plt.figure()
ax1 = fig.add_axes([0, 0, 1, 0.5])
ax2 = fig.add_axes([0, 0.5, 1, 0.5])

ax1.set_yticks([0.5], labels=["very long label"])
ax1.set_ylabel("Y label")

ax2.set_title("Title")
```
