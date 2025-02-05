# 拟合用于异常值检测的模型

我们将使用 `LocalOutlierFactor` 来拟合用于异常值检测的模型，并计算训练样本的预测标签。

```python
clf = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
y_pred = clf.fit_predict(X)
X_scores = clf.negative_outlier_factor_
```
