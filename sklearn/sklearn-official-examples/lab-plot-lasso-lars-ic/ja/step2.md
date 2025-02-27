# データの前処理

StandardScalerメソッドを使ってデータセットをスケーリングし、AIC基準でLassoLarsIC推定器をフィットさせます。

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
```
