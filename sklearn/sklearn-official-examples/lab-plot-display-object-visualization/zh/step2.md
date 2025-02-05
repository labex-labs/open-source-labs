# 创建混淆矩阵显示

使用拟合好的模型，我们计算模型在测试数据集上的预测结果。这些预测结果用于计算混淆矩阵，并通过“混淆矩阵显示”进行绘制。

```python
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay

y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

cm_display = ConfusionMatrixDisplay(cm).plot()
```
