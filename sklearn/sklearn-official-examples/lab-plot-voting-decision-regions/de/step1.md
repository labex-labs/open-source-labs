# Daten laden

Wir werden den Iris-Datensatz mit dem `datasets`-Modul von Scikit-Learn laden. Wir werden nur zwei Merkmale verwenden: Sepal-Länge und Petal-Länge.

```python
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, [0, 2]]
y = iris.target
```
