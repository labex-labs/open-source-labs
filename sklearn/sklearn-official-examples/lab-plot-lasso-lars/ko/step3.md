# Lasso 경로 시각화

Lasso 경로 계산 후 결과를 시각화합니다. 각 특징의 계수를 정규화 매개변수의 함수로 플롯합니다.

```python
import numpy as np
import matplotlib.pyplot as plt

xx = np.sum(np.abs(coefs.T), axis=1)
xx /= xx[-1]

plt.plot(xx, coefs.T)
ymin, ymax = plt.ylim()
plt.vlines(xx, ymin, ymax, linestyle="dashed")
plt.xlabel("|계수 | / 최대 | 계수|")
plt.ylabel("계수")
plt.title("LASSO 경로")
plt.axis("tight")
plt.show()
```
