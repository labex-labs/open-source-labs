# 스케일링

특정 범위로 특징을 스케일링하는 것은 또 다른 일반적인 전처리 기법입니다. 특징들이 서로 다른 스케일을 가지고 있고, 이들을 유사한 범위로 가져오고 싶을 때 유용합니다. `MinMaxScaler`와 `MaxAbsScaler`를 사용하여 스케일링을 수행할 수 있습니다.

```python
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler
import numpy as np

# 샘플 데이터 생성
X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])

# MinMaxScaler 초기화
min_max_scaler = MinMaxScaler()

# 학습 데이터에 대해 fit 및 transform
X_minmax = min_max_scaler.fit_transform(X)

# 변환된 데이터 출력
print(X_minmax)

# MaxAbsScaler 초기화
max_abs_scaler = MaxAbsScaler()

# 학습 데이터에 대해 fit 및 transform
X_maxabs = max_abs_scaler.fit_transform(X)

# 변환된 데이터 출력
print(X_maxabs)
```
