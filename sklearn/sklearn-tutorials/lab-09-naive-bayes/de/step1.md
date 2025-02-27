# Bibliotheken importieren und den Datensatz laden

Lassen Sie uns beginnen, indem wir die erforderlichen Bibliotheken importieren und den Iris-Datensatz laden. Wir werden die Funktion `load_iris` aus dem Modul `sklearn.datasets` verwenden, um den Datensatz zu laden.

```python
from sklearn.datasets import load_iris

# Lade den Iris-Datensatz
iris = load_iris()
X = iris.data  # Merkmale
y = iris.target  # Zielvariable

print("Anzahl der Samples:", X.shape[0])
print("Anzahl der Merkmale:", X.shape[1])
print("Anzahl der Klassen:", len(set(y)))
```
