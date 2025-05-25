# 필요한 라이브러리 가져오기 및 합성 데이터 로드

필요한 라이브러리를 가져오고 합성 데이터를 로드하는 것으로 시작합니다. 합성 랜덤 회귀 데이터 세트를 생성하고 모든 항목이 음수가 아니도록 모든 대상을 변환하고 비선형 대상을 얻기 위해 지수 함수를 적용하여 단순 선형 모델로는 맞출 수 없는 대상을 수정합니다. 그런 다음 로그 함수 (np.log1p) 와 지수 함수 (np.expm1) 를 사용하여 대상을 변환한 후 선형 회귀 모델을 학습하고 예측에 사용합니다.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.compose import TransformedTargetRegressor
from sklearn.linear_model import RidgeCV
from sklearn.metrics import median_absolute_error, r2_score, PredictionErrorDisplay

# 합성 데이터 생성
X, y = make_regression(n_samples=10_000, noise=100, random_state=0)

# 대상 수정
y = np.expm1((y + abs(y.min())) / 200)
y_trans = np.log1p(y)
```
