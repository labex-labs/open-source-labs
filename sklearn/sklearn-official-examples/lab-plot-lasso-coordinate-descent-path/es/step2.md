# Calcular la trayectoria de regularización usando Lasso

En este paso, calcularemos la trayectoria de regularización usando la técnica de Lasso y mostraremos los resultados usando matplotlib.

```python
from sklearn.linear_model import lasso_path
import numpy as np
import matplotlib.pyplot as plt

# Establece el valor de eps
eps = 5e-3

# Calcula la trayectoria de regularización usando Lasso
alphas_lasso, coefs_lasso, _ = lasso_path(X, y, eps=eps)

# Muestra los resultados usando matplotlib
plt.figure(1)
colors = cycle(["b", "r", "g", "c", "k"])
neg_log_alphas_lasso = -np.log10(alphas_lasso)
for coef_l, c in zip(coefs_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coefficients")
plt.title("Lasso Path")
plt.axis("tight")
plt.show()
```
