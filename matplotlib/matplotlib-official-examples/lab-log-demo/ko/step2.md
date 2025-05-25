# Semilogx 플롯

Semilogx 플롯은 x 축에 로그 스케일이 있는 플롯입니다. x 축에 값의 범위가 넓은 데이터를 시각화하는 데 유용합니다.

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
