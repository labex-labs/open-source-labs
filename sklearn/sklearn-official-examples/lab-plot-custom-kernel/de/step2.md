# Daten laden

In diesem Schritt werden wir den Iris-Datensatz mit dem datasets-Modul von scikit-learn laden. Wir werden die ersten beiden Merkmale des Datensatzes auswählen und sie der Variable X zuweisen. Wir werden auch die Zielvariable der Variable Y zuweisen.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
Y = iris.target
```
