# Interaction Constraints in Histogram-based Gradient Boosting Trees

`HistGradientBoostingRegressor` and `HistGradientBoostingClassifier` now support interaction constraints with the `interaction_cst` parameter. For details, see the User Guide.

```python
from sklearn.datasets import load_diabetes
from sklearn.ensemble import HistGradientBoostingRegressor

X, y = load_diabetes(return_X_y=True, as_frame=True)

hist_no_interact = HistGradientBoostingRegressor(
    interaction_cst=[[i] for i in range(X.shape[1])], random_state=0
)
hist_no_interact.fit(X, y)
```
