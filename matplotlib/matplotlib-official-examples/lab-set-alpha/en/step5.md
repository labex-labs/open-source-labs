# Creating a Combined Visualization with Different Alpha Techniques

In this final step, we'll combine multiple techniques to create a more complex visualization that demonstrates both uniform and varying alpha values in one plot.

## Adding a New Cell

Add a new cell to your Jupyter Notebook by clicking the "+" button in the toolbar or pressing "Esc" followed by "b" while in command mode.

## Creating a Combined Visualization

Enter and run the following code in the new cell:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Generate some common data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# First subplot: Fixed alpha for all lines
ax1.plot(x, y1, color='red', linewidth=2, label='sin(x)', alpha=0.7)
ax1.plot(x, y2, color='blue', linewidth=2, label='cos(x)', alpha=0.7)
ax1.plot(x, y3, color='green', linewidth=2, label='sin(x)cos(x)', alpha=0.7)

# Add title and legend to first subplot
ax1.set_title("Multiple Lines with Uniform Alpha")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.5)

# Second subplot: Scatter plot with varying alpha based on y-value
sizes = np.abs(y3 * 100) + 10  # Vary point sizes based on y3
colors = y3  # Use y3 values for coloring

# Calculate varying alpha values between 0.3 and 1.0 based on absolute y3 values
alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))

# Create a scatter plot with varying sizes, colors, and alphas
scatter = ax2.scatter(x, y3, s=sizes, c=colors, cmap='viridis',
                     alpha=alphas)

# Add title and labels to second subplot
ax2.set_title("Scatter Plot with Varying Alpha Based on Y-Value")
ax2.set_xlabel("x")
ax2.set_ylabel("sin(x)cos(x)")
ax2.grid(True, linestyle='--', alpha=0.5)

# Add a colorbar to the second subplot
cbar = plt.colorbar(scatter, ax=ax2)
cbar.set_label('Value of sin(x)cos(x)')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
```

## Understanding the Code and Output

After running the code, you should see a figure with two subplots side by side:

1. **Left Subplot (Uniform Alpha)**: Shows three trigonometric functions plotted with the same alpha value (0.7).

2. **Right Subplot (Varying Alpha)**: Shows a scatter plot where:
   - The x-coordinate is the input value
   - The y-coordinate is sin(x)cos(x)
   - The size of each point varies based on the absolute y-value
   - The color of each point varies based on the y-value
   - The alpha (transparency) of each point varies based on the absolute y-value

Let's analyze the key parts of the code:

1. `fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))` - Creates a figure with two side-by-side subplots.

2. For the first subplot:

   - `ax1.plot(..., alpha=0.7)` - Uses a uniform alpha value for all three lines.

3. For the second subplot:
   - `alphas = 0.3 + 0.7 * (np.abs(y3) / max(np.abs(y3)))` - Calculates varying alpha values between 0.3 and 1.0.
   - `ax2.scatter(..., alpha=alphas)` - Uses varying alpha values for the scatter points.

This combination of techniques demonstrates how alpha values can be used in various ways to enhance visualizations:

- **Uniform alpha** helps when you need to show multiple overlapping elements with equal importance.

- **Varying alpha** helps when you want to emphasize certain data points based on their values.

By mastering these techniques, you can create more effective and visually appealing data visualizations.
