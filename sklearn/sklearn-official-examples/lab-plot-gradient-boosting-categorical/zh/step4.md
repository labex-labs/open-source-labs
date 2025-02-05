# 有序编码管道

我们将创建一个管道，在其中把分类特征当作有序值来处理，并训练一个直方图梯度提升回归器（HistGradientBoostingRegressor）估计器。我们将使用有序编码器（OrdinalEncoder）对分类特征进行编码。

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
