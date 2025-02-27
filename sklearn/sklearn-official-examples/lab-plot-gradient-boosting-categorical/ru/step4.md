# Конвейер ординального кодирования

Мы создадим конвейер, в котором мы будем рассматривать категориальные признаки как ординальные значения и обучать оценщик HistGradientBoostingRegressor. Мы будем использовать OrdinalEncoder для кодирования категориальных признаков.

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
