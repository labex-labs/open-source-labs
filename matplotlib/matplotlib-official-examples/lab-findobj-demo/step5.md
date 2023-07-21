# Creating Different Types of Plots

Matplotlib supports a wide range of plot types, including line plots, scatter plots, bar plots, and more. Here's an example code that creates a scatter plot:

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

# Create a scatter plot
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

# Display the plot
plt.show()
```

In this code, we use the `scatter()` method to create a scatter plot. We generate some random data using the NumPy library and pass it to the `scatter()` method. We also use the `c` parameter to specify the colors of the data points, the `s` parameter to specify the sizes of the data points, and the `alpha` parameter to specify the transparency of the data points.
