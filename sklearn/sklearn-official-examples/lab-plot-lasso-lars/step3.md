# Plot Lasso Path

After computing the Lasso Path, we plot the results. The coefficients for each feature are plotted as a function of the regularization parameter.

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


