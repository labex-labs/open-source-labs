# Creating a Scatter Plot with Alpha Values

In this step, we'll apply our knowledge of alpha values to create a scatter plot. This will demonstrate how transparency can help visualize data density in scatter plots with overlapping points.

## Adding a New Cell

Add a new cell to your Jupyter Notebook by clicking the "+" button in the toolbar or pressing "Esc" followed by "b" while in command mode.

## Creating a Scatter Plot with Transparency

Enter and run the following code in the new cell:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set a random seed for reproducibility
np.random.seed(19680801)

# Create a figure and an axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create two clusters of points
cluster1_x = np.random.normal(0.3, 0.15, 500)
cluster1_y = np.random.normal(0.3, 0.15, 500)

cluster2_x = np.random.normal(0.7, 0.15, 500)
cluster2_y = np.random.normal(0.7, 0.15, 500)

# Combine the clusters
x = np.concatenate([cluster1_x, cluster2_x])
y = np.concatenate([cluster1_y, cluster2_y])

# Create a scatter plot with alpha=0.5
scatter = ax.scatter(x, y, s=30, c='blue', alpha=0.5)

# Add a title and labels
ax.set_title("Scatter Plot with Alpha=0.5 Showing Data Density")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Set axis limits
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Add a grid
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.show()
```

## Understanding the Code and Output

After running the code, you should see a scatter plot with two clusters of points. Each point has a transparency level of 0.5, which allows you to see where points overlap.

Let's break down the key parts of the code:

1. `cluster1_x = np.random.normal(0.3, 0.15, 500)` - Generates 500 random x-coordinates following a normal distribution with mean 0.3 and standard deviation 0.15.

2. `cluster1_y = np.random.normal(0.3, 0.15, 500)` - Generates 500 random y-coordinates for the first cluster.

3. `cluster2_x` and `cluster2_y` - Similarly generate coordinates for the second cluster centered at (0.7, 0.7).

4. `ax.scatter(..., alpha=0.5)` - Creates a scatter plot with points at 50% opacity.

The benefits of using alpha in scatter plots include:

1. **Density Visualization**: Areas where many points overlap appear darker, revealing data density.

2. **Reduced Overplotting**: Without transparency, overlapping points would completely hide each other.

3. **Pattern Recognition**: Transparency helps in identifying clusters and patterns in the data.

Notice how areas with more overlapping points appear darker in the visualization. This is a powerful way to visualize data density without needing additional techniques like density estimation.
