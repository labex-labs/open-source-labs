# Erstellen des Diagramms

Als Nächstes erstellen wir ein einfaches Diagramm, mit dem wir arbeiten können. Wir werden NumPy verwenden, um einige Zufallsdaten zum Plotten zu generieren.

```python
import numpy as np

# Generate random data
np.random.seed(19680801)
data = 100 * np.random.rand(20)

# Create the plot
fig, ax = plt.subplots()
ax.plot(data)
```
