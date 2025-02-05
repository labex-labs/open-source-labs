# 拟合回归模型

现在我们将初始化梯度提升回归器，并使用训练数据对其进行拟合。我们还来看一下测试数据上的均方误差。

```python
reg = ensemble.GradientBoostingRegressor(**params)
reg.fit(X_train, y_train)

mse = mean_squared_error(y_test, reg.predict(X_test))
print("The mean squared error (MSE) on test set: {:.4f}".format(mse))
```
