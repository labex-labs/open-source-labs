# Customizing the Plot

Matplotlib offers a wide range of customization options for plots. Here's an example code that customizes our simple line plot:

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a plot
plt.plot(x, y, color='red', linewidth=2, linestyle='--', marker='o', markersize=8, markerfacecolor='yellow')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Plot')

# Display the plot
plt.show()
```

In this code, we use various parameters of the `plot()` method to customize the plot. We change the color of the line to red, the linewidth to 2, the linestyle to dashed (`--`), the marker to a circle (`o`), the markersize to 8, and the markerfacecolor to yellow.
