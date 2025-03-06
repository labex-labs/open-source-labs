# Advanced Title Positioning with Subplots

In this step, you'll learn advanced techniques for title positioning when working with subplot layouts and axes objects. You'll also learn how to use the `suptitle()` function to add an overall title to a figure with multiple subplots.

## Creating a Figure with Subplots and Individual Titles

Let's create a 2x2 grid of subplots, each with its own title positioned differently:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data and set titles with different positions for each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)

# Top-left subplot: Default centered title
axes[0].set_title('Default (Centered)')

# Top-right subplot: Left-aligned title
axes[1].set_title('Left-Aligned', loc='left')

# Bottom-left subplot: Right-aligned title
axes[2].set_title('Right-Aligned', loc='right')

# Bottom-right subplot: Custom positioned title
axes[3].set_title('Custom Position', y=0.85, loc='center')

# Add spacing between subplots
plt.tight_layout()
plt.show()
```

Run the cell. You should see four subplots, each with a title positioned differently.

## Adding a Figure-Level Title with suptitle()

When working with multiple subplots, you might want to add an overall title for the entire figure. This can be done using the `suptitle()` function:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Flatten the 2D array of axes for easier iteration
axes = axes.flatten()

# Plot data on each subplot
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)
    ax.set_title(f'Subplot {i+1}')

# Add an overall title to the figure
fig.suptitle('Multiple Subplots with an Overall Title', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

Run the cell. You should see four subplots, each with its own title, and an overall title for the figure at the top.

## Combining Axes Titles and Figure Titles

You can combine individual subplot titles with an overall figure title:

```python
# Create a figure with a 2x2 grid of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot data on each subplot with different title positions
axes[0, 0].plot(range(10))
axes[0, 0].grid(True)
axes[0, 0].set_title('Centered Title', loc='center')

axes[0, 1].plot(range(10))
axes[0, 1].grid(True)
axes[0, 1].set_title('Left-Aligned Title', loc='left')

axes[1, 0].plot(range(10))
axes[1, 0].grid(True)
axes[1, 0].set_title('Right-Aligned Title', loc='right')

axes[1, 1].plot(range(10))
axes[1, 1].grid(True)
axes[1, 1].set_title('Lower Title', y=0.85)

# Add an overall title to the figure
fig.suptitle('Advanced Title Positioning Demo', fontsize=16)

# Add spacing between subplots
plt.tight_layout()
# Add top spacing for the suptitle
plt.subplots_adjust(top=0.9)
plt.show()
```

Run the cell. You should see a figure with four subplots, each with a differently positioned title, and an overall title at the top of the figure.

The `suptitle()` function is useful for adding a main title that describes the entire figure, while individual `set_title()` calls on axes objects add more specific titles to each subplot.
