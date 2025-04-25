# 古典的な線形回帰を適合させる

ここでは、古典的な線形回帰を使ってデータを適合させます。これは、scikit - learn の`LinearRegression`クラスを使って行います。その後、テストセットの値を予測し、R2 スコアを計算します。

```python
reg_ols = LinearRegression()
y_pred_ols = reg_ols.fit(X_train, y_train).predict(X_test)
r2_score_ols = r2_score(y_test, y_pred_ols)
print("OLS R2 score", r2_score_ols)
```
