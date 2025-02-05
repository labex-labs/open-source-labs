# 拟合模型

我们使用 scikit-learn 的 `SVC` 类来拟合 SVM 模型。对于无正则化的情况，我们将核函数设置为线性，惩罚参数 `C` 设置为 1；对于正则化的情况，惩罚参数 `C` 设置为 0.05。然后，我们使用模型的系数和截距来计算分离超平面。

```python
for name, penalty in (("unreg", 1), ("reg", 0.05)):
    clf = svm.SVC(kernel="linear", C=penalty)
    clf.fit(X, Y)

    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(-5, 5)
    yy = a * xx - (clf.intercept_[0]) / w[1]
```
