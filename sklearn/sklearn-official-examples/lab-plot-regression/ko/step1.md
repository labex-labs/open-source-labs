# 샘플 데이터 생성

먼저 회귀 문제에 사용할 샘플 데이터를 생성합니다. 1 개의 특징을 가진 40 개의 데이터 포인트 배열을 생성하고, 데이터에 사인 함수를 적용하여 타겟 배열을 만듭니다. 또한 매 5 번째 데이터 포인트에 약간의 노이즈를 추가합니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

np.random.seed(0)
X = np.sort(5 * np.random.rand(40, 1), axis=0)
T = np.linspace(0, 5, 500)[:, np.newaxis]
y = np.sin(X).ravel()

# 타겟에 노이즈 추가
y[::5] += 1 * (0.5 - np.random.rand(8))
```
