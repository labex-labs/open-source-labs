# Left and Right Title Positioning

Matplotlib allows you to position the title to the left or right side of the plot using the `loc` parameter. In this step, you will learn how to align titles to the left and right sides of your plots.

## Creating a Plot with a Left-Aligned Title

Let's create a plot with the title positioned at the left side. In a new cell, enter the following code:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Left-Aligned Title', loc='left')  # Position the title at the left
plt.show()
```

Run the cell. Notice how the title now appears aligned with the left edge of the plot, rather than centered.

The `loc` parameter in the `title()` function determines the horizontal position of the title. By setting `loc='left'`, you're telling Matplotlib to position the title at the left side of the plot.

## Creating a Plot with a Right-Aligned Title

Now, let's create another plot with the title positioned at the right side. In a new cell, enter the following code:

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Right-Aligned Title', loc='right')  # Position the title at the right
plt.show()
```

Run the cell. The title should now appear aligned with the right edge of the plot.

## Comparing Different Title Positions

Let's create a sequence of three plots to compare the different title positions (center, left, and right). In a new cell, enter the following code:

```python
# Create a figure with 3 subplots arranged horizontally
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Plot 1: Center-aligned title (default)
axes[0].plot(range(10))
axes[0].grid(True)
axes[0].set_title('Center Title')

# Plot 2: Left-aligned title
axes[1].plot(range(10))
axes[1].grid(True)
axes[1].set_title('Left Title', loc='left')

# Plot 3: Right-aligned title
axes[2].plot(range(10))
axes[2].grid(True)
axes[2].set_title('Right Title', loc='right')

plt.tight_layout()  # Adjust spacing between subplots
plt.show()
```

Run the cell to see all three title positions side by side. This visual comparison helps you understand how the `loc` parameter affects title positioning.

Note that when working with subplots, we use the `set_title()` method on the individual axis objects rather than the global `plt.title()` function.
