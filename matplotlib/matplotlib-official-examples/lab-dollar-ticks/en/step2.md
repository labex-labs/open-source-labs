# Creating a Basic Financial Plot

Now that we have our data ready, let's create a basic plot to visualize the daily revenue. We'll start with a simple line plot that shows the revenue trend over the 30-day period.

In a new cell in your notebook, add and run the following code:

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)

# Add labels and title
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Revenue', fontsize=12)
ax.set_title('Daily Revenue Over 30 Days', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()

print("Basic plot created successfully!")
```

After running this code, you should see a line plot showing the daily revenue trend. It should look something like this (actual values may vary slightly due to random generation):

![Basic Revenue Plot](https://i.imgur.com/placeholder.png)

Let's break down what we did in this code:

1. `fig, ax = plt.subplots(figsize=(10, 6))` - Created a figure and axes with a size of 10×6 inches
2. `ax.plot(days, daily_revenue, ...)` - Plotted our data with days on the x-axis and revenue on the y-axis
3. `ax.set_xlabel()`, `ax.set_ylabel()`, `ax.set_title()` - Added labels and a title to our plot
4. `ax.grid()` - Added a grid to make the data easier to read
5. `plt.tight_layout()` - Adjusted the padding to ensure everything fits nicely
6. `plt.show()` - Displayed the plot

Notice that the y-axis currently shows plain numbers without dollar signs. In the next step, we'll modify our plot to display proper currency formatting on the y-axis.
