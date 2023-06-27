# Compute Regularization Path Using Lasso

In this step, we will compute the regularization path using the Lasso technique and display the results using matplotlib.

```python
from sklearn.linear_model import lasso_path
import numpy as np
import matplotlib.pyplot as plt

# Set the value of eps
eps = 5e-3

# Compute regularization path using the Lasso
alphas_lasso, coefs_lasso, _ = lasso_path(X, y, eps=eps)

# Display the results using matplotlib
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
