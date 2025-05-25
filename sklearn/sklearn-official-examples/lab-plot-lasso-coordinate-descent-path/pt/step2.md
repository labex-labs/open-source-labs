# Calcular o Caminho de Regularização Usando Lasso

Neste passo, calcularemos o caminho de regularização usando a técnica Lasso e exibiremos os resultados usando matplotlib.

```python
from sklearn.linear_model import lasso_path
import numpy as np
import matplotlib.pyplot as plt

# Definir o valor de eps
eps = 5e-3

# Calcular o caminho de regularização usando o Lasso
alphas_lasso, coefs_lasso, _ = lasso_path(X, y, eps=eps)

# Exibir os resultados usando matplotlib
plt.figure(1)
colors = cycle(["b", "r", "g", "c", "k"])
neg_log_alphas_lasso = -np.log10(alphas_lasso)
for coef_l, c in zip(coefs_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("coeficientes")
plt.title("Caminho Lasso")
plt.axis("tight")
plt.show()
```
