# Graficar el camino de Lasso

Después de calcular el camino de Lasso, graficamos los resultados. Los coeficientes de cada característica se grafican como una función del parámetro de regularización.

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
