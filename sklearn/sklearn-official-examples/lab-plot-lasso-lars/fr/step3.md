# Tracer le chemin de Lasso

Après avoir calculé le chemin de Lasso, nous traçons les résultats. Les coefficients de chaque caractéristique sont tracés en fonction du paramètre de régularisation.

```python
import numpy as np
import matplotlib.pyplot as plt

xx = np.sum(np.abs(coefs.T), axis=1)
xx /= xx[-1]

plt.plot(xx, coefs.T)
ymin, ymax = plt.ylim()
plt.vlines(xx, ymin, ymax, linestyle="dashed")
plt.xlabel("|coef| / max|coef|")
plt.ylabel("Coefficients")
plt.title("LASSO Path")
plt.axis("tight")
plt.show()
```
