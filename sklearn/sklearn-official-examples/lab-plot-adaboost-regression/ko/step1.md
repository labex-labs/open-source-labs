# 데이터 준비

먼저 사인 함수 관계와 일부 가우시안 노이즈를 가진 가상 데이터를 준비합니다. NumPy 의 `linspace()` 함수를 사용하여 0 과 6 사이에 100 개의 균등하게 분포된 값을 가진 1 차원 배열을 생성합니다. 그런 다음 `np.newaxis` 속성을 사용하여 1 차원 배열을 `(100,1)` 형태의 2 차원 배열로 변환합니다. 이 배열에 `sin()` 함수를 적용하고 배열을 6 으로 곱하여 얻은 두 번째 사인파를 더합니다. 마지막으로 NumPy 의 `normal()` 함수를 사용하여 평균 0, 표준 편차 0.1 의 가우시안 노이즈를 추가합니다.

```python
import numpy as np

rng = np.random.RandomState(1)
X = np.linspace(0, 6, 100)[:, np.newaxis]
y = np.sin(X).ravel() + np.sin(6 * X).ravel() + rng.normal(0, 0.1, X.shape[0])
```
