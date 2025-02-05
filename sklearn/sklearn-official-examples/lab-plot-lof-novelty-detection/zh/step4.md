# 评估模型

我们将在测试数据和异常值数据上评估训练好的模型。我们将使用predict方法来预测测试数据和异常值数据的标签。然后，我们将统计测试数据和异常值数据中的错误数量。

```python
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
