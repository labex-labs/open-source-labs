# Creating a Scatter Plot

We will create a scatter plot with X-axis values ranging from 0 to 5 and corresponding Y-axis values. We will use the `scatter` function provided by the `pyplot` module to create the scatter plot.

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a scatter plot
plt.scatter(x, y)

# Adding title and labels to the plot
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```
