# Overlaying the Image on the Plot

Now that we have created our base plot, let's overlay the image on it. We'll use the `figimage` method to add the image to the figure, and we'll make it semi-transparent so that the plot underneath remains visible.

1. Create a new cell in your notebook and enter the following code:

```python
# Create a figure and axes for our plot (same as before)
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)  # x-axis values (0 to 29)
y = x + np.random.randn(30)  # y-axis values (x plus random noise)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')  # Green bars

# Add grid lines
ax.grid(linestyle='--', alpha=0.7)

# Add labels and title
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Image Overlay')

# Load the image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Overlay the image on the plot
# Parameters:
# - im: the image data
# - 25, 25: x and y position in pixels from the bottom left
# - zorder=3: controls the drawing order (higher numbers are drawn on top)
# - alpha=0.5: controls the transparency (0 = transparent, 1 = opaque)
fig.figimage(im, 25, 25, zorder=3, alpha=0.5)

# Display the plot
plt.tight_layout()
plt.show()
```

This code combines what we did in the previous steps and adds the `figimage` method to overlay our image on the plot. Here's a breakdown of the `figimage` parameters:

- `im`: The image data as a NumPy array.
- `25, 25`: The x and y positions in pixels from the bottom left corner of the figure.
- `zorder=3`: Controls the drawing order. Higher numbers are drawn on top of elements with lower numbers.
- `alpha=0.5`: Controls the transparency of the image. A value of 0 is completely transparent, and 1 is completely opaque.

2. Run the cell by pressing Shift+Enter.

The output should show the same bar chart as before, but now with the Matplotlib logo overlaid at the bottom left corner. The logo should be semi-transparent, allowing the plot underneath to remain visible.

3. Let's experiment with different positions and transparency levels. Create a new cell and enter the following code:

```python
# Create a figure and axes for our plot
fig, ax = plt.subplots(figsize=(10, 6))

# Set a random seed for reproducibility
np.random.seed(19680801)

# Generate random data
x = np.arange(30)
y = x + np.random.randn(30)

# Create a bar chart
bars = ax.bar(x, y, color='#6bbc6b')
ax.grid(linestyle='--', alpha=0.7)
ax.set_xlabel('X-axis Label')
ax.set_ylabel('Y-axis Label')
ax.set_title('Bar Chart with Centered Image Overlay')

# Load the image
with cbook.get_sample_data('logo2.png') as file:
    im = image.imread(file)

# Get figure dimensions
fig_width, fig_height = fig.get_size_inches() * fig.dpi

# Calculate center position (this is approximate)
x_center = fig_width / 2 - im.shape[1] / 2
y_center = fig_height / 2 - im.shape[0] / 2

# Overlay the image at the center with higher transparency
fig.figimage(im, x_center, y_center, zorder=3, alpha=0.3)

# Display the plot
plt.tight_layout()
plt.show()
```

This code places the image in the center of the figure with a higher transparency level (alpha=0.3), making it more suitable as a watermark.

4. Run the cell by pressing Shift+Enter.

The output should show the bar chart with the logo centered and more transparent than before, creating a watermark effect.
