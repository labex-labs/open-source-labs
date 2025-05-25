# Errorbars 플롯

Errorbars 플롯은 각 데이터 포인트에 대한 오차 막대를 표시하는 플롯입니다. 데이터 포인트가 음수 값을 가지는 경우 0.1 로 클리핑됩니다.

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
ax4.set(title='Errorbars Plot')
ax4.set_ylim(bottom=0.1)

# Display plot
plt.show()
```
