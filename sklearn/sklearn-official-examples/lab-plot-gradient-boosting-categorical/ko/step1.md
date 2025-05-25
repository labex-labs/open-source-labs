# 데이터셋 로드

Scikit-Learn 의 `fetch_openml` 함수를 사용하여 Ames 주택 데이터셋을 로드하고, 예제 실행 속도를 높이기 위해 특징의 하위 집합을 선택합니다. 또한 범주형 특징을 'category' dtype 으로 변환합니다.

```python
from sklearn.datasets import fetch_openml

X, y = fetch_openml(data_id=42165, as_frame=True, return_X_y=True, parser="pandas")

# 예제 실행 속도를 높이기 위해 X 의 특징 하위 집합만 선택
categorical_columns_subset = [
    "BldgType",
    "GarageFinish",
    "LotConfig",
    "Functional",
    "MasVnrType",
    "HouseStyle",
    "FireplaceQu",
    "ExterCond",
    "ExterQual",
    "PoolQC",
]

numerical_columns_subset = [
    "3SsnPorch",
    "Fireplaces",
    "BsmtHalfBath",
    "HalfBath",
    "GarageCars",
    "TotRmsAbvGrd",
    "BsmtFinSF1",
    "BsmtFinSF2",
    "GrLivArea",
    "ScreenPorch",
]

X = X[categorical_columns_subset + numerical_columns_subset]
X[categorical_columns_subset] = X[categorical_columns_subset].astype("category")
```
