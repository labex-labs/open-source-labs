# 预测异常值

一旦模型拟合完成，我们就可以使用`predict`方法来预测新的观测值是否为异常值。`predict`方法对于内点返回 1，对于异常值返回 -1。

```python
X_test = [5.5, 8.5]
predictions = estimator.predict(X_test)
print(predictions)
```
