# 데이터셋 로드 및 준비

먼저 당뇨병 데이터셋을 로드하고 준비합니다. 이 연습에서는 처음 150 개 샘플만 사용합니다.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets

X, y = datasets.load_diabetes(return_X_y=True)
X = X[:150]
y = y[:150]
```
