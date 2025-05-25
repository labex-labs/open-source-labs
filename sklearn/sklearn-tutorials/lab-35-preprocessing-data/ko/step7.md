# 사용자 정의 변환기 생성

일부 경우, 기존 파이썬 함수를 데이터 정리 또는 처리를 돕는 변환기로 변환하고 싶을 수 있습니다. scikit-learn 의 `FunctionTransformer`를 사용하여 이를 달성할 수 있습니다.

```python
from sklearn.preprocessing import FunctionTransformer
import numpy as np

# 사용자 정의 함수 생성
def custom_function(X):
    return np.log1p(X)

# FunctionTransformer 초기화
transformer = FunctionTransformer(custom_function)

# 샘플 데이터 생성
X = np.array([[0, 1],
              [2, 3]])

# 사용자 정의 함수를 사용하여 데이터 변환
X_transformed = transformer.transform(X)

# 변환된 데이터 출력
print(X_transformed)
```
