# 誤差棒グラフ（Errorbars Plot）

誤差棒グラフは、各データポイントに対する誤差棒を表示するグラフです。データポイントが負の値を持つ場合、その値は0.1にクリップされます。

```python
import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
x = 10.0**np.linspace(0.0, 2.0, 20)
y = x**2.0

# Create figure
fig, ax4 = plt.subplots()

# Set x-axis and y-axis to logarithmic scale
ax4.set_xscale("log", nonpositive='clip')
ax4.set_yscale("log", nonpositive='clip')

# Plot data with error bars
ax4.errorbar(x, y, xerr=0.1 * x, yerr=5.0 + 0.75 * y)

# Set title and y-axis limit
ax4.set(title='誤差棒グラフ（Errorbars Plot）')
ax4.set_ylim(bottom=0.1)

# Display plot
plt.show()
```
