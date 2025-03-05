# Saving the Plot and Creating a Reusable Function

In this final step, we'll create a reusable function to generate currency-formatted plots and save our visualization to a file. This approach makes it easy to apply the same formatting to different financial datasets in the future.

In a new cell in your notebook, add and run the following code:

```python
def create_currency_plot(x_data, y_data, title='Financial Data',
                         xlabel='X-Axis', ylabel='Amount ($)',
                         filename=None, show_stats=True):
    """
    Create a plot with currency formatting on the y-axis.

    Parameters:
    -----------
    x_data : array-like
        Data for the x-axis
    y_data : array-like
        Data for the y-axis (currency values)
    title : str
        Title of the plot
    xlabel : str
        Label for the x-axis
    ylabel : str
        Label for the y-axis
    filename : str, optional
        If provided, save the plot to this filename
    show_stats : bool
        Whether to show statistics (average, min, max)

    Returns:
    --------
    fig, ax : tuple
        The figure and axes objects
    """
    # Import the necessary module for formatting
    import matplotlib.ticker as ticker

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(12, 7))

    # Plot the data
    ax.plot(x_data, y_data, marker='o', linestyle='-', color='blue',
            linewidth=2, markersize=6, label='Data')

    if show_stats:
        # Calculate statistics
        avg_value = np.mean(y_data)
        max_value = np.max(y_data)
        min_value = np.min(y_data)
        max_x = x_data[np.argmax(y_data)]
        min_x = x_data[np.argmin(y_data)]

        # Add a horizontal line for average value
        ax.axhline(y=avg_value, color='r', linestyle='--', alpha=0.7,
                   label=f'Average: ${avg_value:.2f}')

        # Add annotations for max and min values
        ax.annotate(f'Max: ${max_value:.2f}', xy=(max_x, max_value),
                    xytext=(max_x+1, max_value+200),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

        ax.annotate(f'Min: ${min_value:.2f}', xy=(min_x, min_value),
                    xytext=(min_x+1, min_value-200),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

    # Format y-axis with dollar signs
    formatter = ticker.StrMethodFormatter('${x:,.2f}')
    ax.yaxis.set_major_formatter(formatter)

    # Customize tick parameters
    ax.tick_params(axis='both', which='major', labelsize=10)

    # Add labels and title
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')

    # Add grid for better readability
    ax.grid(True, linestyle='--', alpha=0.7)

    # Add legend
    if show_stats:
        ax.legend(loc='best', fontsize=10)

    # Adjust layout
    plt.tight_layout()

    # Save the plot if filename is provided
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Plot saved as '{filename}'")

    return fig, ax

# Use our function to create and save a plot
fig, ax = create_currency_plot(
    days,
    daily_revenue,
    title='Monthly Revenue Report',
    xlabel='Day of Month',
    ylabel='Daily Revenue ($)',
    filename='revenue_plot.png'
)

# Display the plot
plt.show()

print("Function created and plot saved successfully!")
```

After running this code, you should see:

1. A similar plot to what we created in the previous step, but generated using our custom function
2. A message confirming that the plot has been saved to a file named `revenue_plot.png`

The function we created:

- Takes data for x and y axes
- Allows customization of labels and title
- Has an option to save the plot to a file
- Can show or hide statistics like average, min, and max
- Returns the figure and axes objects for further customization if needed

This reusable function makes it easy to create consistently formatted financial plots in the future. You can simply call this function with different datasets, and it will handle all the currency formatting and statistical annotations automatically.

To verify that our plot was saved correctly, let's check if the file exists:

```python
import os
if os.path.exists('revenue_plot.png'):
    print("Plot file exists! Size:", os.path.getsize('revenue_plot.png'), "bytes")
else:
    print("Plot file was not saved correctly.")
```

You should see a message confirming that the file exists and its size.

Congratulations! You have successfully learned how to format plots with dollar signs and create professional-looking financial visualizations using Matplotlib.
