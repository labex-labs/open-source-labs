# Creating a Scatter Plot

We can also use Matplotlib to create a scatter plot. In this example, we will create a scatter plot that shows the relationship between the x and y values.

```python
import matplotlib.pyplot as plt

# x-axis values
x = [1, 2, 3, 4, 5]

# y-axis values
y = [2, 4, 6, 8, 10]

# plotting the points
plt.scatter(x, y)

# setting the title
plt.title("Simple Scatter Plot")

# setting the x-axis label
plt.xlabel("X-axis")

# setting the y-axis label
plt.ylabel("Y-axis")

# displaying the plot
plt.show()
```
