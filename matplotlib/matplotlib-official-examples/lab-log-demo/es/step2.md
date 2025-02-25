# Gráfico Semilogx

El gráfico Semilogx es un gráfico con una escala logarítmica en el eje x. Es útil para visualizar datos que tienen un amplio rango de valores en el eje x.

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
ax2.set(title='Gráfico Semilogx')
ax2.grid()

# Display plot
plt.show()
```
