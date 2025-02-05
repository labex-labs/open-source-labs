# 训练与测试

我们将在训练数据上拟合我们的管道，并使用它来预测 `X_test` 的主题。然后打印我们管道的性能指标。

```python
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print("Classification report:\n\n{}".format(classification_report(y_test, y_pred)))
```
