# 半对数 x 轴图

半对数 x 轴图是一种 x 轴采用对数刻度的图表。它对于可视化在 x 轴上具有大范围值的数据很有用。

```python
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.01, 20.0, 0.01)

# Create figure
fig, ax2 = plt.subplots()

# Plot data on semilogx plot
ax2.semilogx(t, np.sin(2 * np.pi * t))

# Add title and grid to plot
ax2.set(title='Semilogx Plot')
ax2.grid()

# Display plot
plt.show()
```
