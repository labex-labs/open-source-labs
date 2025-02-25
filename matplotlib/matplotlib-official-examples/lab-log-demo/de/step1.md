# Semilogy-Diagramm

Das Semilogy-Diagramm ist ein Diagramm mit logarithmischer Skala auf der y-Achse. Es eignet sich zur Visualisierung von Daten mit einem großen Wertebereich.

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
