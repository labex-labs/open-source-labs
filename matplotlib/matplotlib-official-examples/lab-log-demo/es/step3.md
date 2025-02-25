# Gráfico Loglog

El gráfico Loglog es un gráfico con una escala logarítmica en ambos el eje x y el eje y. Es útil para visualizar datos que tienen un amplio rango de valores en ambos ejes.

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
ax3.set(title='Gráfico Loglog')
ax3.grid()

# Display plot
plt.show()
```
