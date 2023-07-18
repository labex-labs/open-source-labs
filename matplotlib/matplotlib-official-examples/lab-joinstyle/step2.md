# Creating a Graph

To create a graph, we first need to define the data that we want to plot. In this example, we will use the `numpy` library to generate some sample data.

```python
import numpy as np

x = np.linspace(0, 10, 1000)
y = np.sin(x)
```

Next, we create a new figure and axis using `plt.subplots()`. We will set the x and y limits of the graph and then plot the data using `plot()`.

```python
fig, ax = plt.subplots()
ax.set_xlim([0, 10])
ax.set_ylim([-1.2, 1.2])
ax.plot(x, y)
```
