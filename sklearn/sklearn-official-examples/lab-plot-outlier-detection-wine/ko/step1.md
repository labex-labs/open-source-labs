# 라이브러리 가져오기 및 데이터셋 로드

필요한 라이브러리를 가져오고 scikit-learn 의 와인 데이터셋을 로드하여 시작하겠습니다. 와인 데이터셋에는 다양한 종류의 와인에 대한 정보, 즉 화학적 특성이 포함되어 있습니다.

```python
import numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

# 데이터셋 로드
X1 = load_wine()["data"][:, [1, 2]]  # 두 개의 클러스터
X2 = load_wine()["data"][:, [6, 9]]  # "바나나" 모양
```
