# Create the Model

In this step, we will create the SVM-Kernel model with three different kernels: linear, polynomial, and radial basis function (RBF). The linear kernel is used for linearly separable data-points, while the polynomial and RBF kernels are useful for nonlinearly separable data-points.

```python
# fit the model
for kernel in ("linear", "poly", "rbf"):
    clf = svm.SVC(kernel=kernel, gamma=2)
    clf.fit(X, Y)
```
