# Ordinal-Codierungspipeline

Wir werden eine Pipeline erstellen, in der wir die kategorischen Merkmale als ordinalwerte behandeln und einen HistGradientBoostingRegressor-Schätzer trainieren. Wir werden einen OrdinalEncoder verwenden, um die kategorischen Merkmale zu kodieren.

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
