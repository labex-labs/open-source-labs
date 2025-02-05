# 训练随机森林并绘制 ROC 曲线

在这一步中，我们将训练一个随机森林分类器，并将其 ROC 曲线与支持向量分类器（SVC）的 ROC 曲线一起绘制出来。为此，我们将创建一个新的 `RandomForestClassifier` 对象，将其拟合到训练数据上，然后使用这个分类器创建一个新的 `RocCurveDisplay` 对象。我们还将把 `ax` 参数传递给这个函数，以便在同一轴上绘制曲线。最后，我们将调用 `svc_disp` 对象的 `plot()` 方法来绘制 SVC 的 ROC 曲线。

```python
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=10, random_state=42)
rfc.fit(X_train, y_train)

ax = plt.gca()
rfc_disp = RocCurveDisplay.from_estimator(rfc, X_test, y_test, ax=ax, alpha=0.8)
svc_disp.plot(ax=ax, alpha=0.8)
plt.show()
```
