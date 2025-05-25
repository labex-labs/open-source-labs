# Gráfico Semilogx (Semilogx Plot)

O gráfico semilogx é um gráfico com uma escala logarítmica no eixo x. É útil para visualizar dados que possuem uma ampla faixa de valores no eixo x.

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
