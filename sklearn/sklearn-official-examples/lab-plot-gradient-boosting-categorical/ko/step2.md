# 기준 파이프라인 - 범주형 특징 제거

범주형 특징을 제거하고 HistGradientBoostingRegressor 추정기를 학습하는 파이프라인을 생성합니다.

```python
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.compose import make_column_selector

dropper = make_column_transformer(
    ("drop", make_column_selector(dtype_include="category")), remainder="passthrough"
)
hist_dropped = make_pipeline(dropper, HistGradientBoostingRegressor(random_state=42))
```
