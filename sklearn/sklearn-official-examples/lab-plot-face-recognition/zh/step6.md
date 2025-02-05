# 评估模型性能

```python
y_pred = clf.predict(X_test_pca)
print(classification_report(y_test, y_pred, target_names=target_names))
ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation="vertical"
)
```

我们使用测试数据预测目标值，并使用`classification_report()`函数评估模型性能。我们还使用`ConfusionMatrixDisplay()`函数绘制混淆矩阵。
