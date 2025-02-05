# 评估

在这一步中，我们在测试数据集上评估模型的性能。我们使用`sklearn.metrics`模块中的`classification_report`函数为管道模型和逻辑回归模型生成分类报告。

```python
from sklearn import metrics

Y_pred = rbm_features_classifier.predict(X_test)
print(
    "使用RBM特征的逻辑回归:\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)

# 直接在像素上训练逻辑回归分类器
raw_pixel_classifier = clone(logistic)
raw_pixel_classifier.C = 100.0
raw_pixel_classifier.fit(X_train, Y_train)

Y_pred = raw_pixel_classifier.predict(X_test)
print(
    "使用原始像素特征的逻辑回归:\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)
```
