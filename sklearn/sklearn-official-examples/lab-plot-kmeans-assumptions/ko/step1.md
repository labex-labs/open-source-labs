# 데이터 생성

scikit-learn 의 `make_blobs` 함수를 사용하여 다양한 분포를 가진 서로 다른 데이터셋을 생성할 것입니다. 다음 코드 블록에서는 네 가지 데이터셋을 생성합니다.

- 가우시안 볼록 혼합
- 이방성 분포 볼록
- 불균일 분산 볼록
- 불균일 크기 볼록

```python
import numpy as np
from sklearn.datasets import make_blobs

n_samples = 1500
random_state = 170
transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]

X, y = make_blobs(n_samples=n_samples, random_state=random_state)
X_aniso = np.dot(X, transformation)  # 이방성 볼록
X_varied, y_varied = make_blobs(
    n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state
)  # 불균일 분산
X_filtered = np.vstack(
    (X[y == 0][:500], X[y == 1][:100], X[y == 2][:10])
)  # 불균일 크기 볼록
y_filtered = [0] * 500 + [1] * 100 + [2] * 10
```
