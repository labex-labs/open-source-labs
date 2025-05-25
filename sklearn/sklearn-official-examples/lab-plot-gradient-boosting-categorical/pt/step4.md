# Pipeline de Codificação Ordinal

Criaremos um pipeline onde trataremos as características categóricas como valores ordinais e treinaremos um estimador `HistGradientBoostingRegressor`. Usaremos um `OrdinalEncoder` para codificar as características categóricas.

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
