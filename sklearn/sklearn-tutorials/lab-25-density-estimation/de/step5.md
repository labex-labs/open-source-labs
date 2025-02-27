# Visualisieren der Dichteschätzung

Schließlich können wir die Dichteschätzung mithilfe eines Histogramms und der geschätzten Dichtefunktion visualisieren. Wir können das Histogramm der ursprünglichen Daten sowie die geschätzte Dichtefunktion plotten.

```python
import matplotlib.pyplot as plt

bins = np.linspace(-5, 5, 50)
plt.hist(X, bins=bins, density=True, alpha=0.5, label='Histogram')
plt.plot(X, np.exp(scores), color='red', label='Kernel Density Estimate')
plt.legend()
plt.show()
```
