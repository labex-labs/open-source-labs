# Laden oder Generieren kleiner Datensätze

Jetzt müssen wir die kleinen Datensätze laden oder generieren, die wir für dieses Beispiel verwenden werden. Wir werden den Iris-Datensatz, den Digits-Datensatz und zwei Datensätze verwenden, die mit den Funktionen `make_circles` und `make_moons` generiert werden.

```python
iris = datasets.load_iris()
X_digits, y_digits = datasets.load_digits(return_X_y=True)
data_sets = [
    (iris.data, iris.target),
    (X_digits, y_digits),
    datasets.make_circles(noise=0.2, factor=0.5, random_state=1),
    datasets.make_moons(noise=0.3, random_state=0),
]
```
