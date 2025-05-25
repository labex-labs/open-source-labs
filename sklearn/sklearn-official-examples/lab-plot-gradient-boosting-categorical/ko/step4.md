# 순서형 인코딩 파이프라인

범주형 특징을 순서형 값으로 처리하고 HistGradientBoostingRegressor 추정기를 학습하는 파이프라인을 생성합니다. OrdinalEncoder 를 사용하여 범주형 특징을 인코딩합니다.

```python
from sklearn.preprocessing import OrdinalEncoder
import numpy as np

ordinal_encoder = make_column_transformer(
    (
        OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=np.nan),
        make_column_selector(dtype_include="category"),
    ),
    remainder="passthrough",
    verbose_feature_names_out=False,
)

hist_ordinal = make_pipeline(
    ordinal_encoder, HistGradientBoostingRegressor(random_state=42)
)
```
