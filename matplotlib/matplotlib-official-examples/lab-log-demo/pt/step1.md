# Gráfico Semilogy (Semilogy Plot)

O gráfico semilogy é um gráfico com uma escala logarítmica no eixo y. É útil para visualizar dados que possuem uma ampla faixa de valores.

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
