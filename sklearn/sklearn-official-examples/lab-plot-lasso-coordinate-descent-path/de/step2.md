# Berechne den Regularisierungspfad mit Lasso

In diesem Schritt berechnen wir den Regularisierungspfad mit der Lasso-Technik und visualisieren die Ergebnisse mit matplotlib.

```python
from sklearn.linear_model import lasso_path
import numpy as np
import matplotlib.pyplot as plt

# Setze den Wert von eps
eps = 5e-3

# Berechne den Regularisierungspfad mit Lasso
alphas_lasso, coefs_lasso, _ = lasso_path(X, y, eps=eps)

# Zeige die Ergebnisse mit matplotlib an
plt.figure(1)
colors = cycle(["b", "r", "g", "c", "k"])
neg_log_alphas_lasso = -np.log10(alphas_lasso)
for coef_l, c in zip(coefs_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("Koeffizienten")
plt.title("Lasso-Pfad")
plt.axis("tight")
plt.show()
```
