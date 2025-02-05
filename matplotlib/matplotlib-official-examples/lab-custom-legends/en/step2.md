# Composing Custom Legend

In this step, we will create a custom legend using Matplotlib objects. First, we import the `Line2D` class from the `matplotlib.lines` module. Next, we create a list of `Line2D` objects with custom color, width, and label attributes. Finally, we plot the data again using the `plot` function and call `legend()` with the custom lines and corresponding labels.

```python
# Import Line2D class
from matplotlib.lines import Line2D

# Create custom lines
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

# Plot data and generate custom legend
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot'])
```
