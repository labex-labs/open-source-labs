# SGD を使って回帰器を訓練する

次に、SGDRegressor クラスを使って回帰器を訓練します。二乗誤差（squared_error）損失関数と l2 ペナルティを使用します。

```python
# SGD を使って回帰器を訓練する
reg = SGDRegressor(loss="squared_error", penalty="l2", max_iter=100, random_state=42)
reg.fit(X_train, y_train)

# テストセットに対する予測を行う
y_pred = reg.predict(X_test)

# 回帰器の平均二乗誤差を測定する
mse = mean_squared_error(y_test, y_pred)

# 平均二乗誤差を表示する
print("Regressor Mean Squared Error:", mse)
```
