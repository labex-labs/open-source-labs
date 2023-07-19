# Creating a Simple Plot

Now that we have imported Matplotlib, we can use it to create a simple plot. In this example, we will create a line plot that shows the relationship between the x and y values.

```python
import matplotlib.pyplot as plt

# x-axis values
x = [1, 2, 3, 4, 5]

# y-axis values
y = [2, 4, 6, 8, 10]

# plotting the line
plt.plot(x, y)

# setting the title
plt.title("Simple Line Plot")

# setting the x-axis label
plt.xlabel("X-axis")

# setting the y-axis label
plt.ylabel("Y-axis")

# displaying the plot
plt.show()
```
