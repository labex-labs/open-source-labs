# 데이터 로드 및 준비

필요한 라이브러리를 가져오고 iris 데이터셋을 로드하여 시작합니다. 그런 다음 데이터를 섞고 표준화하여 학습에 사용할 준비를 합니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import SGDClassifier

# iris 데이터셋 로드
iris = datasets.load_iris()

# 처음 두 개의 특징 가져오기
X = iris.data[:, :2]
y = iris.target
colors = "bry"

# 데이터 섞기
idx = np.arange(X.shape[0])
np.random.seed(13)
np.random.shuffle(idx)
X = X[idx]
y = y[idx]

# 데이터 표준화
mean = X.mean(axis=0)
std = X.std(axis=0)
X = (X - mean) / std
```
