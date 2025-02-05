# 对新数据进行预测

我们将使用随机森林回归器和多输出回归器对测试数据进行预测。

```python
y_rf = regr_rf.predict(X_test)
y_multirf = regr_multirf.predict(X_test)
```
