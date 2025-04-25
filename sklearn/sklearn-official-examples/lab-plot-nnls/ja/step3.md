# 非負最小二乗回帰を適合させる

ここでは、非負最小二乗回帰を使ってデータを適合させます。これは、scikit - learn の`LinearRegression`クラスを`positive=True`パラメータで使って行います。その後、テストセットの値を予測し、R2 スコアを計算します。

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

reg_nnls = LinearRegression(positive=True)
y_pred_nnls = reg_nnls.fit(X_train, y_train).predict(X_test)
r2_score_nnls = r2_score(y_test, y_pred_nnls)
print("NNLS R2 score", r2_score_nnls)
```
