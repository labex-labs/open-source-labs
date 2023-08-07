# Creating a Bar Plot

We can also use Matplotlib to create a bar plot. In this example, we will create a bar plot that shows the number of apples, bananas, and oranges sold.

```python
import matplotlib.pyplot as plt

# data to plot
apples = 10
bananas = 15
oranges = 5

# creating the bar plot
plt.bar(["Apples", "Bananas", "Oranges"], [apples, bananas, oranges])

# setting the title
plt.title("Simple Bar Plot")

# setting the x-axis label
plt.xlabel("Fruits")

# setting the y-axis label
plt.ylabel("Quantity")

# displaying the plot
plt.show()
```
