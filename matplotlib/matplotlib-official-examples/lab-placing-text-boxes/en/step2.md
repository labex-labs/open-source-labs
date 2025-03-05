# Creating a Basic Histogram

Now that we have our data, let's create a histogram to visualize its distribution. A histogram divides the data into bins (ranges) and shows the frequency of data points within each bin.

## Creating the Histogram

In a new cell in your Jupyter Notebook, enter and run the following code:

```python
# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Display the plot
plt.tight_layout()
plt.show()
```

When you run this cell, you should see a histogram displaying the distribution of your random data. The output will look like a bell-shaped curve (normal distribution) centered near zero.

## Understanding the Code

Let's break down what each line in the code does:

1. `fig, ax = plt.subplots(figsize=(10, 6))`: Creates a figure and axes object. The `figsize` parameter sets the size of the plot in inches (width, height).

2. `histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')`: Creates a histogram of our data `x` with 50 bins. The bins are colored skyblue with black edges.

3. `ax.set_title('Distribution of Random Data', fontsize=16)`: Adds a title to the plot with a font size of 16.

4. `ax.set_xlabel('Value', fontsize=12)` and `ax.set_ylabel('Frequency', fontsize=12)`: Add labels to the x and y axes with a font size of 12.

5. `plt.tight_layout()`: Automatically adjusts the plot to fit the figure area.

6. `plt.show()`: Displays the plot.

The histogram shows how our data is distributed. Since we used `np.random.randn()`, which generates data from a normal distribution, the histogram has a bell shape centered around 0. The height of each bar represents how many data points fall within that range.
