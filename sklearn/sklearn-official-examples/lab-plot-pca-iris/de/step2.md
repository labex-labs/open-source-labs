# Lade den Datensatz

Als nächstes laden wir den Iris-Datensatz mit der Funktion `load_iris()` von scikit-learn. Anschließend trennen wir die Merkmalsvariablen (X) und die Zielvariablen (y) voneinander.

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```
