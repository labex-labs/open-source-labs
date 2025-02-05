# 进行预测

我们将使用这些模型对从0到5的一系列值进行预测。

```python
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
```
