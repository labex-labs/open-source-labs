# Semilogy 플롯

Semilogy 플롯은 y 축에 로그 스케일이 있는 플롯입니다. 값의 범위가 넓은 데이터를 시각화하는 데 유용합니다.

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
