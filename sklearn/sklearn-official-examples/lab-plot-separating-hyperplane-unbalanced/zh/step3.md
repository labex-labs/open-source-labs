# 拟合模型

我们将使用 `svm` 库中的 `SVC` 函数来拟合模型并获得分隔超平面。我们将使用线性核，并将 `C` 设置为 1.0。

```python
clf = svm.SVC(kernel="linear", C=1.0)
clf.fit(X, y)
```
