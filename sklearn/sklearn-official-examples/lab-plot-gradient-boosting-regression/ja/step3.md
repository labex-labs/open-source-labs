# 回帰モデルの適合

ここで、勾配ブースティング回帰器を初期化して、学習データで適合させます。また、テストデータの平均二乗誤差も見てみましょう。

```python
reg = ensemble.GradientBoostingRegressor(**params)
reg.fit(X_train, y_train)

mse = mean_squared_error(y_test, reg.predict(X_test))
print("The mean squared error (MSE) on test set: {:.4f}".format(mse))
```
