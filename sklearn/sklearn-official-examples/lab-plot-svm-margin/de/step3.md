# Modell anpassen

Wir passen das SVM-Modell mit der Klasse `SVC` von scikit-learn an. Wir setzen den Kernel auf linear und den Strafparameter `C` auf 1 für den nicht regulierten Fall und auf 0,05 für den regulierten Fall. Anschließend berechnen wir die trennende Hyperebene mithilfe der Koeffizienten und des Interzepts des Modells.

```python
for name, penalty in (("unreg", 1), ("reg", 0.05)):
    clf = svm.SVC(kernel="linear", C=penalty)
    clf.fit(X, Y)

    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(-5, 5)
    yy = a * xx - (clf.intercept_[0]) / w[1]
```
