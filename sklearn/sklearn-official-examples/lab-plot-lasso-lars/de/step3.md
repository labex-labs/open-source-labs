# Lasso-Pfad plotten

Nachdem wir den Lasso-Pfad berechnet haben, plotten wir die Ergebnisse. Die Koeffizienten für jedes Merkmal werden als Funktion des Regularisierungsparameters geplottet.

```python
import numpy as np
import matplotlib.pyplot as plt

xx = np.sum(np.abs(coefs.T), axis=1)
xx /= xx[-1]

plt.plot(xx, coefs.T)
ymin, ymax = plt.ylim()
plt.vlines(xx, ymin, ymax, linestyle="dashed")
plt.xlabel("|coef| / max|coef|")
plt.ylabel("Koeffizienten")
plt.title("LASSO-Pfad")
plt.axis("tight")
plt.show()
```
