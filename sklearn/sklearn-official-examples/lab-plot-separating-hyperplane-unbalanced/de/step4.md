# Modell mit gewichteten Klassen anpassen

Wir werden das Modell anpassen und die getrennte Hyperebene mit der `SVC`-Funktion aus der `svm`-Bibliothek erhalten. Wir werden einen linearen Kernel verwenden und `class_weight` auf `{1: 10}` setzen. Dadurch wird der kleineren Klasse mehr Gewicht verliehen.

```python
wclf = svm.SVC(kernel="linear", class_weight={1: 10})
wclf.fit(X, y)
```
