# One-Hot-Codierungspipeline

Wir werden eine Pipeline erstellen, in der wir die kategorischen Merkmale mit One-Hot-Codierung kodieren und einen HistGradientBoostingRegressor-Schätzer trainieren.

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
