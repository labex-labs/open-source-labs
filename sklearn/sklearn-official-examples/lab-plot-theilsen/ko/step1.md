# 라이브러리 가져오기 및 데이터셋 생성

먼저, 필요한 라이브러리를 가져오고 회귀 분석을 위한 합성 데이터셋을 생성해 보겠습니다.

```python
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, TheilSenRegressor
from sklearn.linear_model import RANSACRegressor

np.random.seed(0)
n_samples = 200
x = np.random.randn(n_samples)
w = 3.0
c = 2.0
noise = 0.1 * np.random.randn(n_samples)
y = w * x + c + noise
X = x[:, np.newaxis]
```
