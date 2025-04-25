# 绘制 ROC 和 DET 曲线

我们将分别使用 scikit-learn 的`RocCurveDisplay`和`DetCurveDisplay`类来绘制 ROC 曲线和 DET 曲线。`RocCurveDisplay.from_estimator`函数计算 ROC 曲线并将其绘制在给定的轴上。类似地，`DetCurveDisplay.from_estimator`函数计算 DET 曲线并将其绘制在给定的轴上。我们将创建两个子图，一个用于 ROC 曲线，一个用于 DET 曲线，并为每个分类器绘制曲线。

```python
import matplotlib.pyplot as plt
from sklearn.metrics import DetCurveDisplay, RocCurveDisplay

fig, [ax_roc, ax_det] = plt.subplots(1, 2, figsize=(11, 5))

for name, clf in classifiers.items():
    clf.fit(X_train, y_train)

    RocCurveDisplay.from_estimator(clf, X_test, y_test, ax=ax_roc, name=name)
    DetCurveDisplay.from_estimator(clf, X_test, y_test, ax=ax_det, name=name)

ax_roc.set_title("Receiver Operating Characteristic (ROC) curves")
ax_det.set_title("Detection Error Tradeoff (DET) curves")

ax_roc.grid(linestyle="--")
ax_det.grid(linestyle="--")

plt.legend()
plt.show()
```
