# 필요한 라이브러리 가져오기 및 데이터 생성

먼저, 분류에 적합한 데이터 세트를 가져오고 생성해야 합니다. 이 예제에서는 Scikit-learn 의 `make_blobs` 함수를 사용하여 50 개의 분리 가능한 점을 생성합니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import make_blobs

# 50 개의 분리 가능한 점을 생성합니다.
X, Y = make_blobs(n_samples=50, centers=2, random_state=0, cluster_std=0.60)
```
