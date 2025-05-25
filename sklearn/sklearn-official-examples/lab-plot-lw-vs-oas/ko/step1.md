# 라이브러리 가져오기

먼저, 이 실습에 필요한 라이브러리를 가져와야 합니다. `numpy`는 수치 계산, `matplotlib`는 시각화, `scikit-learn`은 공분산 추정에 사용됩니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import toeplitz, cholesky
from sklearn.covariance import LedoitWolf, OAS
```
