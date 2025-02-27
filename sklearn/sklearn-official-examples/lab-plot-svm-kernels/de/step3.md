# Modell erstellen

In diesem Schritt werden wir das SVM-Kernel-Modell mit drei verschiedenen Kernen erstellen: linear, polynomial und radial basis function (RBF). Der lineare Kernel wird für linear trennbare Datenpunkte verwendet, während die polynomialen und RBF-Kerne für nicht linear trennbare Datenpunkte nützlich sind.

```python
# fit the model
for kernel in ("linear", "poly", "rbf"):
    clf = svm.SVC(kernel=kernel, gamma=2)
    clf.fit(X, Y)
```
