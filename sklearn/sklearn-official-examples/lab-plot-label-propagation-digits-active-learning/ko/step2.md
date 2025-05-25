# 데이터 섞기 및 분할

다음으로, 데이터셋을 레이블이 지정된 부분과 레이블이 지정되지 않은 부분으로 섞어 분할합니다. 먼저 레이블이 지정된 데이터 포인트는 10 개로 시작합니다.

```python
import numpy as np

rng = np.random.RandomState(0)
indices = np.arange(len(digits.data))
rng.shuffle(indices)

X = digits.data[indices[:330]]
y = digits.target[indices[:330]]
images = digits.images[indices[:330]]

n_total_samples = len(y)
n_labeled_points = 10
unlabeled_indices = np.arange(n_total_samples)[n_labeled_points:]
```
