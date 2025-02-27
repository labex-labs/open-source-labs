# SVM-Klassifizierer erstellen

In diesem Schritt werden wir eine Instanz des SVM-Klassifizierers erstellen und unsere Daten anpassen. Wir werden den in dem vorherigen Schritt erstellten benutzerdefinierten Kernel verwenden.

```python
clf = svm.SVC(kernel=my_kernel)
clf.fit(X, Y)
```
