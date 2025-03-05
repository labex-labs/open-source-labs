# Adding a Text Box with Statistics

Now that we have a basic histogram, let's enhance it by adding a text box that displays the statistical information about our data. This will make the visualization more informative for viewers.

## Creating the Text Content

First, we need to prepare the text content that will go inside our text box. In a new cell, enter and run the following code:

```python
# Create a string with the statistics
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu,),           # Mean
    r'$\mathrm{median}=%.2f$' % (median,),  # Median
    r'$\sigma=%.2f$' % (sigma,)       # Standard deviation
))

print("Text content for our box:")
print(textstr)
```

You should see output similar to:

```
Text content for our box:
$\mu=-0.31$
$\mathrm{median}=-0.28$
$\sigma=29.86$
```

This code creates a multi-line string containing the mean, median, and standard deviation of our data. Let's examine some interesting aspects of this code:

1. The `\n'.join(...)` method joins multiple strings with a newline character between them.
2. The `r` before each string makes it a "raw" string, which is useful when including special characters.
3. The `$...$` notation is used for LaTeX-style mathematical formatting in matplotlib.
4. `\mu` and `\sigma` are LaTeX symbols for the Greek letters μ (mu) and σ (sigma).
5. `%.2f` is a formatting specifier that displays a floating-point number with two decimal places.

## Creating and Adding the Text Box

Now, let's recreate our histogram and add the text box to it. In a new cell, enter and run the following code:

```python
# Create a new figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data with Statistics', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Define the properties of the text box
properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# Add the text box to the plot
# Position the box in the top left corner (0.05, 0.95) in axes coordinates
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=properties)

# Display the plot
plt.tight_layout()
plt.show()
```

When you run this cell, you should see your histogram with a text box in the top-left corner displaying the statistics.

## Understanding the Text Box Code

Let's break down the important parts of the code that create the text box:

1. `properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)`:

   - This creates a dictionary with properties for the text box.
   - `boxstyle='round'`: Makes the box have rounded corners.
   - `facecolor='wheat'`: Sets the background color of the box to wheat.
   - `alpha=0.5`: Makes the box semi-transparent (50% opacity).

2. `ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=properties)`:
   - This adds text to the axes at position (0.05, 0.95).
   - `transform=ax.transAxes`: This is crucial - it means the coordinates are in axes units (0-1) rather than data units. So (0.05, 0.95) means "5% from the left edge and 95% from the bottom edge of the plot."
   - `fontsize=14`: Sets the font size.
   - `verticalalignment='top'`: Aligns the text so that the top of the text is at the specified y-coordinate.
   - `bbox=properties`: Applies our text box properties.

The text box will remain in the same position relative to the plot axes, even if you zoom in on the plot or change the data range. This is because we used `transform=ax.transAxes`, which uses axes coordinates instead of data coordinates.
