# 데이터셋 생성

두 개의 다변량 공분산 2 차원 데이터셋 X 와 Y 를 생성합니다. 그런 다음 두 데이터셋 간에 가장 많은 공유 분산을 설명하는 각 데이터셋의 성분, 즉 공분산 방향을 추출합니다.

```python
import numpy as np

n = 500
# 2 개의 잠재 변수:
l1 = np.random.normal(size=n)
l2 = np.random.normal(size=n)

latents = np.array([l1, l1, l2, l2]).T
X = latents + np.random.normal(size=4 * n).reshape((n, 4))
Y = latents + np.random.normal(size=4 * n).reshape((n, 4))

X_train = X[: n // 2]
Y_train = Y[: n // 2]
X_test = X[n // 2 :]
Y_test = Y[n // 2 :]

print("Corr(X)")
print(np.round(np.corrcoef(X.T), 2))
print("Corr(Y)")
print(np.round(np.corrcoef(Y.T), 2))
```
