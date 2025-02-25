# Gráfico de barras de error

El gráfico de barras de error es un gráfico que muestra barras de error para cada punto de datos. Si un punto de datos tiene un valor negativo, se recortará a 0,1.

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
ax4.set(title='Gráfico de barras de error')
ax4.set_ylim(bottom=0.1)

# Display plot
plt.show()
```
