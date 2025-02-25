# Loglog-Diagramm

Das Loglog-Diagramm ist ein Diagramm mit logarithmischer Skala auf sowohl der x-Achse als auch der y-Achse. Es eignet sich zur Visualisierung von Daten mit einem großen Wertebereich auf beiden Achsen.

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
