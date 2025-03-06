# Creating a Basic Plot with Random Data

Before we add our image overlay, we need to create a plot that will serve as the base for our visualization. Let's create a simple bar chart using random data.

1. Create a new cell in your notebook and enter the following code:

```python
# Create a figure and axes for our plot
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
ax.set_title('Bar Chart with Random Data')

# Display the plot
plt.tight_layout()
plt.show()
```

This code does the following:

- Creates a figure and axes with a specific size using `plt.subplots()`.
- Sets a random seed to ensure we get the same random values each time we run the code.
- Generates 30 x-values (0 through 29) and corresponding y-values (x plus random noise).
- Creates a bar chart with green bars using `ax.bar()`.
- Adds grid lines to the plot with `ax.grid()`.
- Adds labels for the x-axis, y-axis, and a title for the plot.
- Uses `plt.tight_layout()` to adjust spacing for better appearance.
- Displays the plot using `plt.show()`.

2. Run the cell by pressing Shift+Enter.

The output should display a bar chart with green bars representing the random data. The x-axis shows integers from 0 to 29, and the y-axis shows the corresponding values with random noise added.

This plot will be the foundation on which we'll overlay our image in the next step. Notice how we've stored the figure object in the variable `fig` and the axes object in the variable `ax`. We'll need these variables to add our image overlay.
