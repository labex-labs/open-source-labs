# 데이터셋 로드

scikit-learn 의 `fetch_california_housing` 함수를 사용하여 캘리포니아 주택 데이터셋을 로드합니다. 이 데이터셋은 20,640 개의 샘플과 8 개의 특징으로 구성되어 있습니다.

```python
from sklearn.datasets import fetch_california_housing

X, y = fetch_california_housing(return_X_y=True, as_frame=True)
n_samples, n_features = X.shape

print(f"The dataset consists of {n_samples} samples and {n_features} features")
```
