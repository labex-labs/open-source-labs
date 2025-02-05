# 双对数轴图

双对数轴图是一种在 x 轴和 y 轴上均采用对数刻度的图表。它对于可视化在两个轴上都具有大范围值的数据很有用。

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
