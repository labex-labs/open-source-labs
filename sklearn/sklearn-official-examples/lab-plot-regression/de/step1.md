# Beispiel-Daten generieren

Wir generieren zunächst Beispiel-Daten, die wir für unser Regressionsproblem verwenden. Wir erstellen ein Array mit 40 Datensätzen mit einer Eigenschaft und erstellen dann ein Ziel-Array, indem wir die Sinusfunktion auf die Daten anwenden. Wir fügen auch an jedem fünften Datensatz etwas Rauschen hinzu.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

np.random.seed(0)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
T = np.linspace(0, 5, 500)[:, np.newaxis]
y = np.sin(X).ravel()

# Add noise to targets
y[::5] += 1 * (0.5 - np.random.rand(8))
```
