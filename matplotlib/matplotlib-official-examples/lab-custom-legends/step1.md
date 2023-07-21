# Plotting Lines

In this step, we will plot a set of lines using the Matplotlib library. First, we create some random data using NumPy. Next, we set the color cycle using the `cycler` function to specify the color map. Finally, we plot the data using the `plot` function and call `legend()` to generate the legend.

```python
import matplotlib.pyplot as plt
import numpy as np

# Set random state for reproducibility
np.random.seed(19680801)

# Create random data
N = 10
data = (np.geomspace(1, 10, 100) + np.random.randn(N, 100)).T

# Set color cycle
cmap = plt.cm.coolwarm
plt.rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))

# Plot data and generate legend
fig, ax = plt.subplots()
lines = ax.plot(data)
ax.legend()
```
