# Composing Custom Legend with Different Matplotlib Objects

In this step, we will create a custom legend using different Matplotlib objects, including `Line2D` and `Patch`. First, we import the `Patch` class from the `matplotlib.patches` module. Next, we create a list of `Line2D` and `Patch` objects with custom attributes. Finally, we call `legend()` with the custom objects and corresponding labels.

```python
# Import Line2D and Patch classes
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# Create legend elements
legend_elements = [Line2D([0], [0], color='b', lw=4, label='Line'),
                   Line2D([0], [0], marker='o', color='w', label='Scatter',
                          markerfacecolor='g', markersize=15),
                   Patch(facecolor='orange', edgecolor='r',
                         label='Color Patch')]

# Plot data and generate custom legend
fig, ax = plt.subplots()
ax.legend(handles=legend_elements, loc='center')
```
