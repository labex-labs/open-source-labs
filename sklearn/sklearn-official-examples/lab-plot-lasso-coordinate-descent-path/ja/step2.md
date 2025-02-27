# ラッソを使って正則化パスを計算する

このステップでは、ラッソ手法を使って正則化パスを計算し、matplotlibを使って結果を表示します。

```python
from sklearn.linear_model import lasso_path
import numpy as np
import matplotlib.pyplot as plt

# epsの値を設定する
eps = 5e-3

# ラッソを使って正則化パスを計算する
alphas_lasso, coefs_lasso, _ = lasso_path(X, y, eps=eps)

# matplotlibを使って結果を表示する
plt.figure(1)
colors = cycle(["b", "r", "g", "c", "k"])
neg_log_alphas_lasso = -np.log10(alphas_lasso)
for coef_l, c in zip(coefs_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("係数")
plt.title("ラッソパス")
plt.axis("tight")
plt.show()
```
