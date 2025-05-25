# 거리 메트릭

거리 메트릭은 두 개의 객체 간의 유사성을 측정하는 함수입니다. 이러한 메트릭은 음수가 아니고, 대칭이며, 삼각 부등식과 같은 특정 조건을 만족합니다.

일부 인기 있는 거리 메트릭으로는 유클리드 거리, 맨해튼 거리, 민코프스키 거리가 있습니다.

`pairwise_distances` 함수를 사용하여 두 개의 샘플 집합 간의 쌍별 거리를 계산해 보겠습니다.

```python
import numpy as np
from sklearn.metrics import pairwise_distances

X = np.array([[2, 3], [3, 5], [5, 8]])
Y = np.array([[1, 0], [2, 1]])

# X 와 Y 사이의 쌍별 거리 계산
distances = pairwise_distances(X, Y, metric='manhattan')
print(distances)
```

출력:

```
array([[4., 2.],
       [7., 5.],
       [12., 10.]])
```
