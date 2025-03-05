# Formatting Y-Axis Labels with Dollar Signs

Now that we have our basic plot, let's format the y-axis labels to display dollar signs. This will make our financial data more readable and professionally presented.

To format the tick labels on the y-axis, we'll use Matplotlib's `ticker` module, which provides various formatting options. Specifically, we'll use the `StrMethodFormatter` class to create a custom formatter for our y-axis.

In a new cell in your notebook, add and run the following code:

```python
# Import the necessary module for formatting
import matplotlib.ticker as ticker

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the daily revenue data
ax.plot(days, daily_revenue, marker='o', linestyle='-', color='blue', linewidth=2, markersize=6)

# Format y-axis with dollar signs
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)

# Add labels and title
ax.set_xlabel('Day', fontsize=12)
ax.set_ylabel('Revenue ($)', fontsize=12)
ax.set_title('Daily Revenue Over 30 Days', fontsize=14, fontweight='bold')

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Display the plot
plt.tight_layout()
plt.show()

print("Plot with dollar-formatted y-axis created!")
```

After running this code, you should see a new plot with dollar signs on the y-axis labels.

Let's explain the key part of this code:

```python
formatter = ticker.StrMethodFormatter('${x:,.2f}')
ax.yaxis.set_major_formatter(formatter)
```

Here's what this formatting string does:

- `$` - Adds a dollar sign at the beginning of each label
- `{x:,.2f}` - Formats the number with:
  - `,` - Comma as a thousands separator (e.g., 1,000 instead of 1000)
  - `.2f` - Two decimal places (e.g., $1,234.56)

This formatter applies to all the major tick labels on the y-axis. Notice how the plot now clearly indicates that the values are in dollars, making it much more appropriate for financial data visualization.
