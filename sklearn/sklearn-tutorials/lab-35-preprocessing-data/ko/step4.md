# 범주형 특징 인코딩

범주형 특징은 머신러닝 알고리즘에 사용되기 전에 숫자 값으로 인코딩되어야 합니다. scikit-learn 의 `OrdinalEncoder`와 `OneHotEncoder`를 사용하여 범주형 특징을 인코딩할 수 있습니다.

```python
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
import numpy as np

# 샘플 데이터 생성
X = [['male', 'from US', 'uses Safari'],
     ['female', 'from Europe', 'uses Firefox']]

# OrdinalEncoder 초기화
ordinal_encoder = OrdinalEncoder()

# 학습 데이터에 대해 fit 및 transform
X_encoded = ordinal_encoder.fit_transform(X)

# 변환된 데이터 출력
print(X_encoded)

# OneHotEncoder 초기화
onehot_encoder = OneHotEncoder()

# 학습 데이터에 대해 fit 및 transform
X_onehot = onehot_encoder.fit_transform(X)

# 변환된 데이터 출력
print(X_onehot.toarray())
```
