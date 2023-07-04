# Customizing Line Properties

Matplotlib allows you to customize various line properties, such as linewidth, dash style, and color. Let's demonstrate some ways to set line properties:

```python
x = np.arange(0, 5, 0.1)
line, = plt.plot(x, np.sin(x), '-')

# Using the Line2D instance's setter method
line.set linewidth(2.0)  # Set the linewidth property of the line to 2.0

# Using the pyplot.setp function
plt.setp(line, color='r', linewidth=2.0)  # Set the color and linewidth properties using the setp function

plt.show()
```

Explanation:

- We create an array `x` and compute the corresponding y-values using the `np.sin` function.
- The `plot` function is called to create a line plot.
- We use the `set` method of the `Line2D` instance to set the linewidth property of the line to 2.0.
- Alternatively, we can use the `setp` function to set multiple properties of the line, such as color and linewidth, using keyword arguments.
