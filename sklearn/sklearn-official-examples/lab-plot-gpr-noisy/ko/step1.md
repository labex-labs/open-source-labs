# 데이터 생성

이 단계에서는 사인 함수를 사용하여 단일 특징을 가진 데이터를 생성합니다.

```python
import numpy as np

def target_generator(X, add_noise=False):
    target = 0.5 + np.sin(3 * X)
    if add_noise:
        rng = np.random.RandomState(1)
        target += rng.normal(0, 0.3, size=target.shape)
    return target.squeeze()

X = np.linspace(0, 5, num=30).reshape(-1, 1)
y = target_generator(X, add_noise=False)
```
