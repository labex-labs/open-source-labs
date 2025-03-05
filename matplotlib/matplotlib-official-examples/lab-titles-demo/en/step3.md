# Custom Title Vertical Positioning

Sometimes you might want to adjust the vertical position of your title. In this step, you'll learn how to manually control the vertical (y-axis) position of your plot titles.

## Understanding Y-Position in Titles

The vertical position of a title can be adjusted using the `y` parameter in the `title()` function. The `y` parameter accepts values in normalized coordinates, where:

- `y=1.0` (default) places the title at the top of the plot
- `y>1.0` places the title above the top of the plot
- `y<1.0` places the title below the top of the plot, moving it closer to the plot content

## Creating a Plot with Custom Title Y-Position

Let's create a plot with the title positioned higher than the default. In a new cell, enter the following code:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Higher Title Position', y=1.1)  # Position the title higher
plt.show()
```

Run the cell. Notice how the title now appears slightly higher above the plot compared to the default position.

Now, let's create a plot with the title positioned lower than the default:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Lower Title Position', y=0.9)  # Position the title lower
plt.show()
```

Run the cell. The title should now appear closer to the plot content.

## Comparing Different Y-Positions

Let's create multiple plots side by side to compare different vertical title positions:

```python
# Create a figure with 3 subplots arranged horizontally
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: Default Y-position
axes[0].plot(range(10))
axes[0].grid(True)
axes[0].set_title('Default Position (y=1.0)')

# Plot 2: Higher Y-position
axes[1].plot(range(10))
axes[1].grid(True)
axes[1].set_title('Higher Position', y=1.15)

# Plot 3: Lower Y-position
axes[2].plot(range(10))
axes[2].grid(True)
axes[2].set_title('Lower Position', y=0.85)

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
```

Run the cell to see all three vertical positions side by side. This comparison helps you understand how the `y` parameter affects the vertical position of the title.

## Combining Horizontal and Vertical Positioning

You can combine the `loc` parameter (for horizontal alignment) with the `y` parameter (for vertical position) to place your title exactly where you want it:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Custom Positioned Title', loc='right', y=1.1)  # Right-aligned and higher
plt.show()
```

Run the cell. The title should now appear aligned with the right edge of the plot and positioned higher than the default.
