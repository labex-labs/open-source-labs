# 다항식 특징 생성

입력 데이터의 비선형 특징을 고려하여 모델의 복잡성을 높이는 것이 때로는 유용합니다. scikit-learn 의 `PolynomialFeatures`를 사용하여 다항식 특징을 생성할 수 있습니다.

```python
from sklearn.preprocessing import PolynomialFeatures
import numpy as np

# 샘플 데이터 생성
X = np.array([[0, 1],
              [2, 3],
              [4, 5]])

# PolynomialFeatures 초기화
poly = PolynomialFeatures(2)

# 학습 데이터에 대해 fit 및 transform
X_poly = poly.fit_transform(X)

# 변환된 데이터 출력
print(X_poly)
```
