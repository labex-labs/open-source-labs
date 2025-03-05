# Customizing the Text Box

Now that we have successfully added a text box to our plot, let's explore various customization options to make it more visually appealing and suitable for different contexts.

## Experimenting with Different Styles

Let's create a function to make it easier to experiment with different text box styles. In a new cell, enter and run the following code:

```python
def plot_with_textbox(boxstyle, facecolor, alpha, position=(0.05, 0.95)):
    """
    Create a histogram with a custom text box.

    Parameters:
    boxstyle (str): Style of the box ('round', 'square', 'round4', etc.)
    facecolor (str): Background color of the box
    alpha (float): Transparency of the box (0-1)
    position (tuple): Position of the box in axes coordinates (x, y)
    """
    # Create figure and plot
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(x, bins=50, color='skyblue', edgecolor='black')

    # Set title and labels
    ax.set_title(f'Text Box Style: {boxstyle}', fontsize=16)
    ax.set_xlabel('Value', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)

    # Create text box properties
    box_props = dict(boxstyle=boxstyle, facecolor=facecolor, alpha=alpha)

    # Add text box
    ax.text(position[0], position[1], textstr, transform=ax.transAxes,
            fontsize=14, verticalalignment='top', bbox=box_props)

    plt.tight_layout()
    plt.show()
```

Now, let's use this function to try different box styles. In a new cell, enter and run:

```python
# Try a square box with light green color
plot_with_textbox('square', 'lightgreen', 0.7)

# Try a rounded box with light blue color
plot_with_textbox('round', 'lightblue', 0.5)

# Try a box with extra rounded corners
plot_with_textbox('round4', 'lightyellow', 0.6)

# Try a sawtooth style box
plot_with_textbox('sawtooth', 'lightcoral', 0.4)
```

When you run this cell, you'll see four different plots, each with a different text box style.

## Changing the Text Box Position

The position of a text box can be crucial for visualization. Let's place text boxes in different corners of the plot. In a new cell, enter and run:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.flatten()  # Flatten to easily iterate

# Define positions for the four corners
positions = [
    (0.05, 0.95),  # Top left
    (0.95, 0.95),  # Top right
    (0.05, 0.05),  # Bottom left
    (0.95, 0.05)   # Bottom right
]

# Define alignments for each position
alignments = [
    ('top', 'left'),          # Top left
    ('top', 'right'),         # Top right
    ('bottom', 'left'),       # Bottom left
    ('bottom', 'right')       # Bottom right
]

# Corner labels
corner_labels = ['Top Left', 'Top Right', 'Bottom Left', 'Bottom Right']

# Create four plots with text boxes in different corners
for i, ax in enumerate(axes):
    # Plot histogram
    ax.hist(x, bins=50, color='skyblue', edgecolor='black')

    # Set title
    ax.set_title(f'Text Box in {corner_labels[i]}', fontsize=14)

    # Create text box properties
    box_props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    # Add text box
    ax.text(positions[i][0], positions[i][1], textstr,
            transform=ax.transAxes, fontsize=12,
            verticalalignment=alignments[i][0],
            horizontalalignment=alignments[i][1],
            bbox=box_props)

plt.tight_layout()
plt.show()
```

This code creates a 2x2 grid of histograms, each with a text box in a different corner.

## Understanding Text Box Positioning

There are several key parameters that control text box positioning:

1. **Position coordinates**: The `(x, y)` coordinates determine where the text box is placed. When using `transform=ax.transAxes`, these are in axes coordinates where `(0, 0)` is the bottom-left corner and `(1, 1)` is the top-right corner.

2. **Vertical alignment**: The `verticalalignment` parameter controls how the text is aligned vertically relative to the y-coordinate:

   - `'top'`: The top of the text is at the specified y-coordinate.
   - `'center'`: The center of the text is at the specified y-coordinate.
   - `'bottom'`: The bottom of the text is at the specified y-coordinate.

3. **Horizontal alignment**: The `horizontalalignment` parameter controls how the text is aligned horizontally relative to the x-coordinate:
   - `'left'`: The left edge of the text is at the specified x-coordinate.
   - `'center'`: The center of the text is at the specified x-coordinate.
   - `'right'`: The right edge of the text is at the specified x-coordinate.

These alignment options are particularly important when placing text in corners. For example, in the top-right corner, you would want to use `horizontalalignment='right'` so the right edge of the text aligns with the right edge of the plot.
