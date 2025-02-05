# 获取异常值分数

除了预测异常值，我们还可以使用`negative_outlier_factor_`属性获取每个观测值的异常值分数。较低的异常值分数表示更高的异常程度。

```python
outlier_scores = estimator.negative_outlier_factor_
print(outlier_scores)
```
