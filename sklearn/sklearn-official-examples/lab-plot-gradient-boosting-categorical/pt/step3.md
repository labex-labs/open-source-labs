# Pipeline de Codificação One-Hot

Criaremos um pipeline onde codificaremos as características categóricas usando a codificação one-hot e treinaremos um estimador `HistGradientBoostingRegressor`.

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
