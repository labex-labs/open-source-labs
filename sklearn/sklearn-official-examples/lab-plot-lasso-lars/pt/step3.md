# Plotar o Caminho Lasso

Após calcular o Caminho Lasso, plotamos os resultados. Os coeficientes para cada característica são plotados em função do parâmetro de regularização.

```python
import numpy as np
import matplotlib.pyplot as plt

xx = np.sum(np.abs(coefs.T), axis=1)
xx /= xx[-1]

plt.plot(xx, coefs.T)
ymin, ymax = plt.ylim()
plt.vlines(xx, ymin, ymax, linestyle="dashed")
plt.xlabel("|coef| / max|coef|")
plt.ylabel("Coeficientes")
plt.title("Caminho Lasso")
plt.axis("tight")
plt.show()
```
