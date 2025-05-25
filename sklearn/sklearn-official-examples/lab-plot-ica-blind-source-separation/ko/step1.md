# 샘플 데이터 생성

세 개의 독립적인 구성 요소로 이루어진 샘플 혼합 신호를 생성합니다. 신호에 노이즈를 추가하고 데이터를 표준화합니다. 또한 세 개의 독립적인 구성 요소를 혼합하는 혼합 행렬을 생성합니다.

```python
import numpy as np
from scipy import signal

np.random.seed(0)
n_samples = 2000
time = np.linspace(0, 8, n_samples)

s1 = np.sin(2 * time)  # 신호 1 : 사인파 신호
s2 = np.sign(np.sin(3 * time))  # 신호 2 : 사각파 신호
s3 = signal.sawtooth(2 * np.pi * time)  # 신호 3: 톱니파 신호

S = np.c_[s1, s2, s3]
S += 0.2 * np.random.normal(size=S.shape)  # 노이즈 추가

S /= S.std(axis=0)  # 데이터 표준화
# 데이터 혼합
A = np.array([[1, 1, 1], [0.5, 2, 1.0], [1.5, 1.0, 2.0]])  # 혼합 행렬
X = np.dot(S, A.T)  # 관측치 생성
```
