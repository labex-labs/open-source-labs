# 샘플 데이터 생성

사인파 목표 함수로 구성되고 다섯 번째 데이터 포인트마다 강한 노이즈가 추가된 데이터셋을 생성합니다.

```python
import numpy as np

# 샘플 데이터 생성
rng = np.random.RandomState(42)
X = 5 * rng.rand(10000, 1)
y = np.sin(X).ravel()

# 목표에 노이즈 추가
y[::5] += 3 * (0.5 - rng.rand(X.shape[0] // 5))

X_plot = np.linspace(0, 5, 100000)[:, None]
```
