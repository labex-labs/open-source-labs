# Lasso 경로 계산

다음으로, LARS 알고리즘을 사용하여 Lasso 경로를 계산합니다. Scikit-Learn 의 `linear_model` 모듈에서 `lars_path` 함수를 사용하여 Lasso 경로를 계산합니다. 이 함수는 입력 특징, 목표 변수 및 방법을 매개변수로 받습니다. 이 경우 L1 정규화를 위해 "lasso" 방법을 사용합니다.

```python
from sklearn import linear_model

_, _, coefs = linear_model.lars_path(X, y, method="lasso", verbose=True)
```
