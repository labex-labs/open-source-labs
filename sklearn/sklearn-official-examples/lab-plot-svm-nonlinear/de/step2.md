# Daten generieren

In diesem Schritt werden wir die Daten für das Training und die Prüfung des SVM-Klassifikators generieren. Wir werden 300 zufällige Datenpunkte mit zwei Merkmalen generieren. Das vorherzusagende Ziel ist ein XOR der Eingaben.

```python
np.random.seed(0)
X = np.random.randn(300, 2)
Y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0)
```
