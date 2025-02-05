# Creating a Simple Plot

The most basic plot in Matplotlib is a line plot. You can create a line plot using the `plot()` method. Here's an example code that creates a simple line plot:

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')

# Display the plot
plt.show()
```

In this code, we first define our data points as two lists `x` and `y`. We then create a plot using the `plot()` method and pass in our data points. We then add labels to the X and Y axes and a title to the plot using the `xlabel()`, `ylabel()`, and `title()` methods. Finally, we display the plot using the `show()` method.
