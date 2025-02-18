# Das Modell trainieren

In diesem Schritt werden wir den SVM-Klassifikator mit RBF-Kernel (Radial Basis Function - Kernel) anhand der generierten Daten trainieren.

```python
clf = svm.NuSVC(gamma="auto")
clf.fit(X, Y)
```
