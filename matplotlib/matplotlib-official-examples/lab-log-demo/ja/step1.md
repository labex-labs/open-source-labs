# 半対数グラフ（Semilogy Plot）

半対数グラフは、y 軸に対数スケールを持つグラフです。値の範囲が広いデータを視覚化するのに便利です。

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
ax1.set(title='半対数グラフ（Semilogy Plot）')
ax1.grid()

# Display plot
plt.show()
```
