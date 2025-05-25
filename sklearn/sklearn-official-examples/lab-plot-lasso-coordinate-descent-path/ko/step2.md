# Lasso 를 이용한 정규화 경로 계산

이 단계에서는 Lasso 기법을 사용하여 정규화 경로를 계산하고 matplotlib 를 사용하여 결과를 표시합니다.

```python
from sklearn.linear_model import lasso_path
import numpy as np
import matplotlib.pyplot as plt

# eps 값 설정
eps = 5e-3

# Lasso 를 이용하여 정규화 경로 계산
alphas_lasso, coefs_lasso, _ = lasso_path(X, y, eps=eps)

# matplotlib 를 사용하여 결과 표시
plt.figure(1)
colors = cycle(["b", "r", "g", "c", "k"])
neg_log_alphas_lasso = -np.log10(alphas_lasso)
for coef_l, c in zip(coefs_lasso, colors):
    l1 = plt.plot(neg_log_alphas_lasso, coef_l, c=c)

plt.xlabel("-Log(alpha)")
plt.ylabel("계수")
plt.title("Lasso 경로")
plt.axis("tight")
plt.show()
```
