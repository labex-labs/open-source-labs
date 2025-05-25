# 당뇨병 데이터셋 로드

먼저, scikit-learn 에서 당뇨병 데이터셋을 로드하고 학습 및 테스트 데이터셋으로 분할합니다.

```python
from sklearn import datasets
import numpy as np

X, y = datasets.load_diabetes(return_X_y=True)
indices = (0, 1)

X_train = X[:-20, indices]
X_test = X[-20:, indices]
y_train = y[:-20]
y_test = y[-20:]
```
