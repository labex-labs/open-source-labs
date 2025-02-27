# Laden des Datensatzes

Als nächstes laden wir den Datensatz, mit dem wir arbeiten werden. Wir können für diese Übung jeden beliebigen Datensatz verwenden.

```python
from sklearn.datasets import load_iris

# Lade den Iris-Datensatz
iris = load_iris()

# Teile die Daten in Merkmale und Ziel auf
X = iris.data
y = iris.target
```
