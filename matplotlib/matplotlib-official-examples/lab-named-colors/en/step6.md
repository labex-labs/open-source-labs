# Creating a Pie Chart

We can also use Matplotlib to create a pie chart. In this example, we will create a pie chart that shows the percentage of people who prefer different types of pizza.

```python
import matplotlib.pyplot as plt

# data to plot
sizes = [30, 40, 10, 20]
labels = ["Pepperoni", "Mushroom", "Onion", "Sausage"]

# creating the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# setting the title
plt.title("Simple Pie Chart")

# displaying the plot
plt.show()
```
