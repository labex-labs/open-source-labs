# 绘制 ROC 曲线

接下来，我们将使用 `RocCurveDisplay.from_estimator` 函数绘制 ROC 曲线。此函数将训练好的分类器、测试数据集和真实标签作为输入，并返回一个可用于绘制 ROC 曲线的对象。然后，我们将调用 `show()` 方法来显示该图。

```python
svc_disp = RocCurveDisplay.from_estimator(svc, X_test, y_test)
svc_disp.show()
```
