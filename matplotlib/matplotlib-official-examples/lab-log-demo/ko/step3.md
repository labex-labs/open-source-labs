# Loglog 플롯

Loglog 플롯은 x 축과 y 축 모두에 로그 스케일이 있는 플롯입니다. 두 축 모두에 값의 범위가 넓은 데이터를 시각화하는 데 유용합니다.

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
