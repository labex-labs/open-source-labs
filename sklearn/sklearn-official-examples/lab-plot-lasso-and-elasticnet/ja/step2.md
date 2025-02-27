# Lasso

このステップでは、Lasso 回帰モデルを使用してデータセットの疎な係数を推定する方法を示します。正則化パラメータ `alpha` の固定値を使用します。実際には、最適なパラメータ `alpha` は、`LassoCV` に `TimeSeriesSplit` 交差検証戦略を渡すことで選択する必要があります。この例を簡単で高速に実行するために、ここでは直接 alpha の最適値を設定します。

```python
from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score
from time import time

t0 = time()
lasso = Lasso(alpha=0.14).fit(X_train, y_train)
print(f"Lasso fit done in {(time() - t0):.3f}s")

y_pred_lasso = lasso.predict(X_test)
r2_score_lasso = r2_score(y_test, y_pred_lasso)
print(f"Lasso r^2 on test data : {r2_score_lasso:.3f}")
```
