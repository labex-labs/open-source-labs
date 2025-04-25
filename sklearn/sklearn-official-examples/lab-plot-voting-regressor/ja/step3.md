# 回帰器の学習

次に、勾配ブースティング回帰器、ランダムフォレスト回帰器、線形回帰を初期化します。次に、これら 3 つの回帰器を使って投票回帰器を構築します。

```python
# Train classifiers
reg1 = GradientBoostingRegressor(random_state=1)
reg2 = RandomForestRegressor(random_state=1)
reg3 = LinearRegression()

reg1.fit(X, y)
reg2.fit(X, y)
reg3.fit(X, y)

ereg = VotingRegressor([("gb", reg1), ("rf", reg2), ("lr", reg3)])
ereg.fit(X, y)
```
