# Laden der Daten

Als nächstes laden wir den Iris-Datensatz aus Scikit-learn und wählen nur die ersten beiden Merkmale für die Visualisierung aus.

```python
iris = datasets.load_iris()
X = iris.data[:, :2]
y = iris.target
```
