# Creating a Simple Line Plot

We will create a simple line plot with X-axis values ranging from 0 to 5 and corresponding Y-axis values. We will use the `plot` function provided by the `pyplot` module to create the line plot.

```python
# Creating X-axis values
x = np.arange(0, 5, 0.1)

# Creating Y-axis values
y = np.sin(x)

# Creating a line plot
plt.plot(x, y)

# Adding title and labels to the plot
plt.title('Simple Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Displaying the plot
plt.show()
```
