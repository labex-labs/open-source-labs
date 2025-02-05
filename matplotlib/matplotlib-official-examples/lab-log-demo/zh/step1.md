# 半对数 y 轴图

半对数 y 轴图是一种 y 轴采用对数刻度的图表。它对于可视化具有大范围值的数据很有用。

```python
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.01, 20.0, 0.01)

# Create figure
fig, ax1 = plt.subplots()

# Plot data on semilogy plot
ax1.semilogy(t, np.exp(-t / 5.0))

# Add title and grid to plot
ax1.set(title='Semilogy Plot')
ax1.grid()

# Display plot
plt.show()
```
