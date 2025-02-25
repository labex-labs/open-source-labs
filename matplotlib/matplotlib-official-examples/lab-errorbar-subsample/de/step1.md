# Bibliotheken importieren und Daten generieren

Zunächst müssen wir die erforderlichen Bibliotheken importieren und einige Beispiel-Daten generieren, mit denen wir arbeiten können. In diesem Beispiel werden wir `numpy` verwenden, um die Daten zu generieren, und `matplotlib`, um sie zu visualisieren.

```python
import matplotlib.pyplot as plt
import numpy as np

# Beispiel-Daten
x = np.arange(0.1, 4, 0.1)
y1 = np.exp(-1.0 * x)
y2 = np.exp(-0.5 * x)

# Beispiel-Werte für variable Fehlerbalken
y1err = 0.1 + 0.1 * np.sqrt(x)
y2err = 0.1 + 0.1 * np.sqrt(x/2)
```
