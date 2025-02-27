# Modell anpassen

Wir werden das Modell anpassen und die getrennte Hyperebene mit der `SVC`-Funktion aus der `svm`-Bibliothek erhalten. Wir werden einen linearen Kernel verwenden und `C` auf 1.0 setzen.

```python
clf = svm.SVC(kernel="linear", C=1.0)
clf.fit(X, y)
```
