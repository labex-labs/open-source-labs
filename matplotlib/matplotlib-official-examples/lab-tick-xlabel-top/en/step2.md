# Creating a Basic Plot with Default Settings

Now that we have Matplotlib imported, let's create a simple plot with default settings to understand how the axes and tick labels are positioned by default.

## Understanding Matplotlib Components

In Matplotlib, plots consist of several components:

- **Figure**: The overall container for the plot
- **Axes**: The area where data is plotted with its own coordinate system
- **Axis**: The number-line-like objects that define the coordinate system
- **Ticks**: The marks on the axes that denote specific values
- **Tick Labels**: The text labels that indicate the value at each tick

By default, x-axis tick labels appear at the bottom of the plot.

## Creating a Simple Plot

In a new cell in your notebook, let's create a simple line plot:

```python
# Create a figure and a set of axes
fig, ax = plt.subplots(figsize=(8, 5))

# Generate some data
x = np.arange(0, 10, 1)
y = np.sin(x)

# Plot the data
ax.plot(x, y, marker='o', linestyle='-', color='blue', label='sin(x)')

# Add a title and labels
ax.set_title('A Simple Sine Wave Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis (sin(x))')

# Add a grid and legend
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

# Display the plot
plt.show()

print("Notice that the x-axis tick labels are at the bottom of the plot by default.")
```

When you run this code, you will see a sine wave plot with the x-axis tick labels at the bottom of the plot, which is the default position in Matplotlib.

Take a moment to observe how the plot is structured and where the tick labels are positioned. This understanding will help us appreciate the changes we make in the next step.
