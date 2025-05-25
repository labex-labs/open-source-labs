# 원 - 핫 인코딩 파이프라인

범주형 특징을 원 - 핫 인코딩하고 HistGradientBoostingRegressor 추정기를 학습하는 파이프라인을 생성합니다.

```python
from sklearn.preprocessing import OneHotEncoder

one_hot_encoder = make_column_transformer(
    (
        OneHotEncoder(sparse_output=False, handle_unknown="ignore"),
        make_column_selector(dtype_include="category"),
    ),
    remainder="passthrough",
)

hist_one_hot = make_pipeline(
    one_hot_encoder, HistGradientBoostingRegressor(random_state=42)
)
```
