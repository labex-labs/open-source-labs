# データの前処理

StandardScaler メソッドを使ってデータセットをスケーリングし、AIC 基準で LassoLarsIC 推定器をフィットさせます。

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
```
