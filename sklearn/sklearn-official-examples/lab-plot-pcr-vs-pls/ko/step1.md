# 데이터셋 생성

두 개의 특징을 가진 간단한 데이터셋을 생성합니다. NumPy 라이브러리를 사용하여 데이터셋을 생성하고 Matplotlib 라이브러리를 사용하여 플롯합니다.

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.RandomState(0)
n_samples = 500
cov = [[3, 3], [3, 4]]
X = rng.multivariate_normal(mean=[0, 0], cov=cov, size=n_samples)
plt.scatter(X[:, 0], X[:, 1], alpha=0.3, label="samples")
plt.gca().set(
    aspect="equal",
    title="주성분을 가진 2 차원 데이터셋",
    xlabel="첫 번째 특징",
    ylabel="두 번째 특징",
)
plt.legend()
plt.show()
```
