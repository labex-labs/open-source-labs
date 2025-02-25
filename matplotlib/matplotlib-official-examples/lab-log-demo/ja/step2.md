# 半対数グラフ（Semilogx Plot）

半対数グラフは、x軸に対数スケールを持つグラフです。x軸に値の範囲が広いデータを視覚化するのに便利です。

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
ax2.set(title='半対数グラフ（Semilogx Plot）')
ax2.grid()

# Display plot
plt.show()
```
