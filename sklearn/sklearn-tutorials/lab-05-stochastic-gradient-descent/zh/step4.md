# 使用随机梯度下降（SGD）训练回归器

接下来，我们将使用 SGDRegressor 类训练一个回归器。我们将使用平方误差（squared_error）损失函数和 L2 正则化。

```python
# 使用随机梯度下降训练回归器
reg = SGDRegressor(loss="squared_error", penalty="l2", max_iter=100, random_state=42)
reg.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = reg.predict(X_test)

# 评估回归器的均方误差
mse = mean_squared_error(y_test, y_pred)

# 打印均方误差
print("回归器均方误差：", mse)
```
