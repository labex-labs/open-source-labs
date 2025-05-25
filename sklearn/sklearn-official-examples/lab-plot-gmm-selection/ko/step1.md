# 데이터 생성

`numpy.random.randn`으로 반환되는 표준 정규 분포에서 무작위로 샘플링하여 두 개의 구성 요소 (각각 `n_samples` 개 포함) 를 생성합니다. 한 구성 요소는 구형이지만 이동 및 재조정됩니다. 다른 구성 요소는 더 일반적인 공분산 행렬을 갖도록 변형됩니다.

```python
import numpy as np

n_samples = 500
np.random.seed(0)
C = np.array([[0.0, -0.1], [1.7, 0.4]])
component_1 = np.dot(np.random.randn(n_samples, 2), C)  # 일반적인 공분산 행렬
component_2 = 0.7 * np.random.randn(n_samples, 2) + np.array([-4, 1])  # 구형

X = np.concatenate([component_1, component_2])
```
