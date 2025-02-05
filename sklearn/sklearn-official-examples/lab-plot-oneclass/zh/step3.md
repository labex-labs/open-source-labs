# 计算错误数量

我们将计算模型在训练数据、常规新观测值和异常新观测值上所犯错误的数量。

```python
# 统计错误数量
n_error_train = y_pred_train[y_pred_train == -1].size
n_error_test = y_pred_test[y_pred_test == -1].size
n_error_outliers = y_pred_outliers[y_pred_outliers == 1].size
```
