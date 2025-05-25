# 데이터 로드 및 전처리

먼저 scikit-learn 에서 손글씨 숫자 데이터셋을 로드하고 훈련 데이터와 테스트 데이터로 분할합니다. 또한 데이터를 평균 0, 분산 1 로 스케일링합니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 숫자 데이터셋 로드
X, y = datasets.load_digits(return_X_y=True)

# 데이터를 훈련 및 테스트 세트로 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 데이터를 평균 0, 분산 1 로 스케일링
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```
