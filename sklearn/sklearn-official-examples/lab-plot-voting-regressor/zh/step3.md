# 训练回归器

现在，让我们初始化一个梯度提升回归器、一个随机森林回归器和一个线性回归器。接下来，我们将使用这三个回归器来构建投票回归器。

```python
# 训练分类器
reg1 = GradientBoostingRegressor(random_state=1)
reg2 = RandomForestRegressor(random_state=1)
reg3 = LinearRegression()

reg1.fit(X, y)
reg2.fit(X, y)
reg3.fit(X, y)

ereg = VotingRegressor([("gb", reg1), ("rf", reg2), ("lr", reg3)])
ereg.fit(X, y)
```
