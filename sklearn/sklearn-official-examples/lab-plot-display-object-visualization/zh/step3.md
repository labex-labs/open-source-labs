# 创建ROC曲线显示

ROC曲线需要估计器的概率或非阈值化决策值。由于逻辑回归提供了一个决策函数，我们将使用它来绘制ROC曲线。

```python
from sklearn.metrics import roc_curve
from sklearn.metrics import RocCurveDisplay

y_score = clf.decision_function(X_test)

fpr, tpr, _ = roc_curve(y_test, y_score, pos_label=clf.classes_[1])
roc_display = RocCurveDisplay(fpr=fpr, tpr=tpr).plot()
```
