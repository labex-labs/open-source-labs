# 进行预测

在这一步中，我们将使用上一步创建的模型进行预测。我们将使用`np.arange`创建一个新的数组，其值从 -100 到 100，间隔为 0.01，然后使用我们模型的`predict`方法来预测输出。

```python
# 进行预测
X_test = np.arange(-100.0, 100.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
y_3 = regr_3.predict(X_test)
```
