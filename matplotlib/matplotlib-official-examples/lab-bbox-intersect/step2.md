# Set up the rectangle

We will define the position and dimensions of the rectangle using `left`, `bottom`, `width`, and `height` variables. Then, we will create the rectangle using `Rectangle` class and add it to the plot using `add_patch` method.

```python
left, bottom, width, height = (-1, -1, 2, 2)
rect = plt.Rectangle((left, bottom), width, height,
                     facecolor="black", alpha=0.1)

fig, ax = plt.subplots()
ax.add_patch(rect)
```
