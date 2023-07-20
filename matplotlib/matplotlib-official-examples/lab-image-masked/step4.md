# Creating a Scatter Plot

In addition to line plots, Matplotlib also allows us to create scatter plots. Scatter plots are useful for visualizing the relationship between two variables.

```python
# Create the data
x = np.random.rand(50)
y = np.random.rand(50)

# Create the scatter plot
plt.scatter(x, y)

# Add title and axis labels
plt.title('Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
```
