# Creating a Reusable Function for Image Overlays

To make our code more reusable, let's create a function that can add an image overlay to any Matplotlib figure. This way, we can easily apply the same effect to different plots.

1. Create a new cell in your notebook and enter the following code:

```python
def add_image_overlay(fig, image_path, x_pos=25, y_pos=25, alpha=0.5, zorder=3):
    """
    Add an image overlay to a matplotlib figure.

    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        The figure to add the image to
    image_path : str
        Path to the image file
    x_pos : int
        X position in pixels from the bottom left
    y_pos : int
        Y position in pixels from the bottom left
    alpha : float
        Transparency level (0 to 1)
    zorder : int
        Drawing order (higher numbers are drawn on top)

    Returns:
    --------
    fig : matplotlib.figure.Figure
        The figure with the image overlay
    """
    # Load the image
    with cbook.get_sample_data(image_path) as file:
        im = image.imread(file)

    # Add the image to the figure
    fig.figimage(im, x_pos, y_pos, zorder=zorder, alpha=alpha)

    return fig

# Example usage: Create a scatter plot with an image overlay
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data for a scatter plot
x = np.random.rand(50) * 10
y = np.random.rand(50) * 10

# Create a scatter plot
ax.scatter(x, y, s=100, c=np.random.rand(50), cmap='viridis', alpha=0.7)
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Scatter Plot with Image Overlay')

# Add the image overlay using our function
add_image_overlay(fig, 'logo2.png', x_pos=50, y_pos=50, alpha=0.4)

# Display the plot
plt.tight_layout()
plt.show()
```

This code defines a function called `add_image_overlay` that:

- Takes parameters for the figure, image path, position, transparency, and z-order.
- Loads the specified image.
- Adds the image to the figure using `figimage`.
- Returns the modified figure.

After defining the function, we demonstrate its use by creating a scatter plot with random data and adding the Matplotlib logo as an overlay.

2. Run the cell by pressing Shift+Enter.

The output should show a scatter plot with randomly positioned and colored points, and the Matplotlib logo overlaid at position (50, 50) with 40% opacity.

3. Let's try one more example with a line plot. Create a new cell and enter the following code:

```python
# Example usage: Create a line plot with an image overlay
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data for a line plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a line plot
ax.plot(x, y, linewidth=2, color='#d62728')
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Sine Wave with Image Overlay')
ax.set_ylim(-1.5, 1.5)

# Add the image overlay using our function
# Place it in the bottom right corner
fig_width, fig_height = fig.get_size_inches() * fig.dpi
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)
    x_pos = fig_width - im.shape[1] - 50  # 50 pixels from the right edge

add_image_overlay(fig, 'logo2.png', x_pos=x_pos, y_pos=50, alpha=0.6)

# Display the plot
plt.tight_layout()
plt.show()
```

This code creates a line plot showing a sine wave, and adds the Matplotlib logo in the bottom right corner of the plot.

4. Run the cell by pressing Shift+Enter.

The output should show a line plot of a sine wave with the Matplotlib logo overlaid in the bottom right corner at 60% opacity.

These examples demonstrate how our `add_image_overlay` function can be used to easily add image overlays to different types of plots, making it a versatile tool for customizing visualizations.
