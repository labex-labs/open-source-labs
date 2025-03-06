# Understanding Alpha Values in Matplotlib

In this first step, we will create a Jupyter Notebook and learn how to set up a basic visualization with alpha values.

## Creating Your First Jupyter Notebook Cell

In this cell, we'll import the necessary libraries and create two overlapping circles with different alpha values to demonstrate transparency.

```python
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(6, 4))

# Create a circle with alpha=1.0 (completely opaque)
circle1 = plt.Circle((0.5, 0.5), 0.3, color='blue', alpha=1.0, label='Opaque (alpha=1.0)')

# Create a circle with alpha=0.5 (semi-transparent)
circle2 = plt.Circle((0.7, 0.5), 0.3, color='red', alpha=0.5, label='Semi-transparent (alpha=0.5)')

# Add circles to the axes
ax.add_patch(circle1)
ax.add_patch(circle2)

# Set axis limits
ax.set_xlim(0, 1.2)
ax.set_ylim(0, 1)

# Add a title and legend
ax.set_title('Demonstrating Alpha Values in Matplotlib')
ax.legend(loc='upper right')

# Show the plot
plt.show()
```

Once you've entered this code in the cell, run it by pressing Shift+Enter or clicking the "Run" button in the toolbar.

## Understanding the Output

You should see two overlapping circles:

- The blue circle on the left is completely opaque (alpha=1.0)
- The red circle on the right is semi-transparent (alpha=0.5)

Notice how you can see the blue circle through the red one where they overlap. This is the effect of setting the alpha value to 0.5 for the red circle.

Alpha values control transparency in visualizations and can help when:

- Showing overlapping data points
- Highlighting certain elements
- Reducing visual clutter in dense plots
- Creating layered visualizations

Let's continue to explore more applications of alpha values in the next step.
