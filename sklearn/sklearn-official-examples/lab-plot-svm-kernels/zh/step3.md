# 创建模型

在这一步中，我们将使用三种不同的核创建支持向量机核（SVM-Kernel）模型：线性核、多项式核和径向基函数（RBF）核。线性核用于线性可分的数据点，而多项式核和RBF核对于非线性可分的数据点很有用。

```python
# fit the model
for kernel in ("linear", "poly", "rbf"):
    clf = svm.SVC(kernel=kernel, gamma=2)
    clf.fit(X, Y)
```
