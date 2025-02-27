# Calculer le chemin de régularisation à l'aide de la Lasso

Dans cette étape, nous allons calculer le chemin de régularisation à l'aide de la technique Lasso et afficher les résultats à l'aide de matplotlib.

```python
from sklearn.linear_model import lasso_path
import numpy as np
import matplotlib.pyplot as plt

# Définir la valeur de eps
eps = 5e-3

# Calculer le chemin de régularisation à l'aide de la Lasso
alphas_lasso, coefs_lasso, _ = lasso_path(X, y, eps=eps)

# Afficher les résultats à l'aide de matplotlib
plt.figure(1)
colors = cycle(["b", "r", "g", "c", "k"])
neg_log_alphas_lasso = -np.log10(alphas_lasso)
for coef_l, c in zip(coefs_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coefficients")
plt.title("Chemin de la Lasso")
plt.axis("tight")
plt.show()
```
