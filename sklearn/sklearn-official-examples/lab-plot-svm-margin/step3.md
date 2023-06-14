# Fit the Model

We fit the SVM model using scikit-learn's `SVC` class. We set the kernel to linear and the penalty parameter `C` to 1 for the unregularized case and 0.05 for the regularized case. We then calculate the separating hyperplane using the coefficients and the intercept of the model.

```python
for name, penalty in (("unreg", 1), ("reg", 0.05)):
    clf = svm.SVC(kernel="linear", C=penalty)
    clf.fit(X, Y)

    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(-5, 5)
    yy = a * xx - (clf.intercept_[0]) / w[1]
```


