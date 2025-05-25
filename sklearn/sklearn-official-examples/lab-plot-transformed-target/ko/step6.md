# Ames 주택 데이터 로드 및 전처리

Ames 주택 데이터 세트를 로드하고 숫자 열만 유지하고 NaN 또는 Inf 값이 있는 열을 제거하여 전처리합니다. 예측할 대상은 각 주택의 판매 가격입니다.

```python
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import quantile_transform

ames = fetch_openml(name="house_prices", as_frame=True, parser="pandas")

# 숫자 열만 유지
X = ames.data.select_dtypes(np.number)

# NaN 또는 Inf 값이 있는 열 제거
X = X.drop(columns=["LotFrontage", "GarageYrBlt", "MasVnrArea"])

# 가격을 k 달러로 표시
y = ames.target / 1000
y_trans = quantile_transform(
    y.to_frame(), n_quantiles=900, output_distribution="normal", copy=True
).squeeze()
```
