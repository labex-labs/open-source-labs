# Moving the X-Axis Tick Labels to the Top

Now that we understand the default positioning of tick labels, let's move the x-axis tick labels to the top of the plot.

## Understanding Tick Parameters

Matplotlib provides the `tick_params()` method to control the appearance of ticks and tick labels. This method allows us to:

- Show/hide ticks and tick labels
- Change their position (top, bottom, left, right)
- Adjust their size, color, and other properties

## Creating a Plot with X-Axis Tick Labels at the Top

Let's create a new plot with the x-axis tick labels moved to the top:

```python
# Create a new figure and a set of axes
fig, ax = plt.subplots(figsize=(8, 5))

# Generate some data
x = np.arange(0, 10, 1)
y = np.cos(x)

# Plot the data
ax.plot(x, y, marker='s', linestyle='-', color='green', label='cos(x)')

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',         # Apply changes to the x-axis
    top=True,         # Show ticks on the top side
    labeltop=True,    # Show tick labels on the top side
    bottom=False,     # Hide ticks on the bottom side
    labelbottom=False # Hide tick labels on the bottom side
)

# Add a title and labels
ax.set_title('Cosine Wave with X-Axis Tick Labels at the Top')
ax.set_xlabel('X-axis (now at the top!)')
ax.set_ylabel('Y-axis (cos(x))')

# Add a grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Display the plot
plt.show()

print("Now the x-axis tick labels are at the top of the plot!")
```

When you run this code, you will see a cosine wave plot with the x-axis tick labels at the top of the plot.

Notice how the `tick_params()` method is used with several parameters:

- `axis='x'`: Specifies that we want to modify the x-axis
- `top=True` and `labeltop=True`: Makes ticks and labels visible on the top
- `bottom=False` and `labelbottom=False`: Hides ticks and labels on the bottom

This gives us a clean view of the data with x-axis labels positioned at the top rather than the bottom.
