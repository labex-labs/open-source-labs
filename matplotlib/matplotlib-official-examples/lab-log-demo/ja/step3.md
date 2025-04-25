# 対数対数グラフ（Loglog Plot）

対数対数グラフは、x 軸と y 軸の両方に対数スケールを持つグラフです。両軸に値の範囲が広いデータを視覚化するのに便利です。

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
ax3.set(title='対数対数グラフ（Loglog Plot）')
ax3.grid()

# Display plot
plt.show()
```
