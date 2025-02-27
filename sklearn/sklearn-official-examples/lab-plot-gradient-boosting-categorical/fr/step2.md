# Pipeline de base - Suppression des variables catégorielles

Nous allons créer un pipeline dans lequel nous supprimons les variables catégorielles et entraîner un estimateur HistGradientBoostingRegressor.

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
