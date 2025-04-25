# 生成混淆矩阵

我们将使用 scikit-learn 中的 ConfusionMatrixDisplay 类生成一个混淆矩阵。该混淆矩阵会展示每个类别的正确预测和错误预测的数量。

```python
np.set_printoptions(precision=2)
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    X_test,
    y_test,
    display_labels=class_names,
    cmap=plt.cm.Blues,
    normalize=None,
)
```
