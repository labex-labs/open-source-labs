# Loglog Plot

The loglog plot is a plot with a logarithmic scale on both the x-axis and y-axis. It is useful for visualizing data that has a large range of values on both axes.

```python
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.01, 20.0, 0.01)

# Create figure
fig, ax3 = plt.subplots()

# Plot data on loglog plot
ax3.loglog(t, 20 * np.exp(-t / 10.0))

# Set x-axis scale to base 2
ax3.set_xscale('log', base=2)

# Add title and grid to plot
ax3.set(title='Loglog Plot')
ax3.grid()

# Display plot
plt.show()
```
