# 预测并评估模型

我们将使用训练好的模型来预测测试子集中样本的数字值。然后，我们将使用`sklearn.metrics`中的`metrics.classification_report()`和`metrics.ConfusionMatrixDisplay.from_predictions()`方法来评估模型。

```python
predicted = clf.predict(X_test)

print(
    f"Classification report for classifier {clf}:\n"
    f"{metrics.classification_report(y_test, predicted)}\n"
)

disp = metrics.ConfusionMatrixDisplay.from_predictions(y_test, predicted)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")
```
