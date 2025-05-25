# 누락된 값의 보간

데이터 세트에서 누락된 값은 머신 러닝 알고리즘에 문제를 일으킬 수 있습니다. scikit-learn 의 `impute` 모듈에서 제공하는 방법을 사용하여 누락된 값을 처리할 수 있습니다. 여기서는 누락된 값을 보간하기 위해 `SimpleImputer`를 사용합니다.

```python
from sklearn.impute import SimpleImputer
import numpy as np

# 누락된 값이 있는 샘플 데이터 생성
X = np.array([[1., 2., np.nan],
              [3., np.nan, 5.],
              [np.nan, 4., 6.]])

# SimpleImputer 초기화
imputer = SimpleImputer()

# 학습 데이터에 대해 fit 및 transform
X_imputed = imputer.fit_transform(X)

# 변환된 데이터 출력
print(X_imputed)
```
