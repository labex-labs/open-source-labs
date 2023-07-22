# Customize Spines for Bottom and Left Sides

In the second subplot, we will display spines only on the bottom and left sides of the plot. We can hide the spines on the right and top sides of the plot using the `set_visible` method.

```python
ax1.plot(x, y)
ax1.set_title('Bottom-Left Spines')

# Hide the right and top spines
ax1.spines.right.set_visible(False)
ax1.spines.top.set_visible(False)
```
