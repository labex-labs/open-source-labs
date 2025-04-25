# 情報基準を使った Lasso の選択

正則化パラメータ alpha の最適値を選択するために、赤池情報量基準 (AIC) またはベイズ情報量基準 (BIC) を使用する Lasso 推定器を提供するために、`sklearn.linear_model` からの `LassoLarsIC` 関数を使用します。まず、AIC 基準を使って Lasso モデルをフィットさせます。

```python
import time
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LassoLarsIC
from sklearn.pipeline import make_pipeline

start_time = time.time()
lasso_lars_ic = make_pipeline(StandardScaler(), LassoLarsIC(criterion="aic")).fit(X, y)
fit_time = time.time() - start_time
```
