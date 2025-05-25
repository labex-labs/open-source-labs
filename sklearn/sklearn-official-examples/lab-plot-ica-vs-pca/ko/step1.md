# 샘플 데이터 생성

이 단계에서는 매우 비정규적인 과정, 자유도가 낮은 2 개의 학생 t 분포를 사용하여 샘플 데이터를 생성합니다.

```python
import numpy as np

from sklearn.decomposition import PCA, FastICA

rng = np.random.RandomState(42)
S = rng.standard_t(1.5, size=(20000, 2))
S[:, 0] *= 2.0

# 혼합 데이터
A = np.array([[1, 1], [0, 2]])  # 혼합 행렬

X = np.dot(S, A.T)  # 관측치 생성
```
