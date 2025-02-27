# Beispiel-Daten generieren

Zunächst generieren wir einen Beispiel-Datensatz, der aus 40 zufälligen Werten zwischen 0 und 5 besteht. Anschließend berechnen wir die Sinusfunktion jedes Wertes und fügen jedem 5. Wert etwas Rauschen hinzu.

```python
import numpy as np

# Generate sample data
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()

# add noise to targets
y[::5] += 3 * (0.5 - np.random.rand(8))
```
