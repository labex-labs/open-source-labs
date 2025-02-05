# 独热编码管道

我们将创建一个管道，在其中对分类特征进行独热编码，并训练一个直方图梯度提升回归器（HistGradientBoostingRegressor）估计器。

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
