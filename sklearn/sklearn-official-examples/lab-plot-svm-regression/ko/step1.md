# 샘플 데이터 생성

먼저, 0 과 5 사이의 40 개의 랜덤 값으로 구성된 샘플 데이터 세트를 생성합니다. 그런 다음 각 값의 사인 함수를 계산하고 매 5 번째 값에 약간의 노이즈를 추가합니다.

```python
import numpy as np

# 샘플 데이터 생성
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()

# 대상에 노이즈 추가
y[::5] += 3 * (0.5 - np.random.rand(8))
```
