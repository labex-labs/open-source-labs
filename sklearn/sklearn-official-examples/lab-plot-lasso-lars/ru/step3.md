# Построение графика пути Lasso

После вычисления пути Lasso мы строим график результатов. Коэффициенты для каждого признака строятся в виде функции от параметра регуляризации.

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
