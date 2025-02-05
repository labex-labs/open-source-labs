# 对加权类别拟合模型

我们将使用 `svm` 库中的 `SVC` 函数对模型进行拟合并获得分隔超平面。我们将使用线性核，并将 `class_weight` 设置为 `{1: 10}`。这将给较小的类别赋予更大的权重。

```python
wclf = svm.SVC(kernel="linear", class_weight={1: 10})
wclf.fit(X, y)
```
