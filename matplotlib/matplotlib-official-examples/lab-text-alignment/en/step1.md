# Creating a Rectangle

We will begin by creating a rectangle in the plot using `Rectangle()` function of `matplotlib.patches` module. After creating the rectangle, we will set its horizontal and vertical limits using `set_xlim()` and `set_ylim()` functions. Finally, we will add the rectangle to the plot.

```python
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots()

# Build a rectangle in axes coords
left, width = .25, .5
bottom, height = .25, .5
right = left + width
top = bottom + height
p = Rectangle((left, bottom), width, height, fill=False)
ax.add_patch(p)

# Set the horizontal and vertical limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.show()
```
