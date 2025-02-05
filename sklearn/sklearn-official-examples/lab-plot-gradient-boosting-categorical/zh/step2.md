# 基线管道 - 丢弃分类特征

我们将创建一个管道，在其中丢弃分类特征，并训练一个直方图梯度提升回归器（HistGradientBoostingRegressor）估计器。

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
