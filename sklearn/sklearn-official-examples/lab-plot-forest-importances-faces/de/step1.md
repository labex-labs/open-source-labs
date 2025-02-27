# Daten laden und Modellanpassung

Wir beginnen mit dem Laden des Olivetti Faces-Datensatzes und begrenzen den Datensatz, sodass er nur die ersten fünf Klassen enthält. Anschließend trainieren wir einen Random Forest auf dem Datensatz und bewerten die auf Unreinheit basierende Merkmalswichtigkeit. Wir werden die Anzahl der Kerne festlegen, die für die Aufgaben verwendet werden sollen.

```python
from sklearn.datasets import fetch_olivetti_faces

# Wir wählen die Anzahl der Kerne aus, die zur parallelen Anpassung
# des Waldmodells verwendet werden sollen. `-1` bedeutet, alle verfügbaren Kerne zu verwenden.
n_jobs = -1

# Laden des Gesichtsdatensatzes
data = fetch_olivetti_faces()
X, y = data.data, data.target

# Begrenzen des Datensatzes auf 5 Klassen.
mask = y < 5
X = X[mask]
y = y[mask]

# Ein Random Forest-Klassifizierer wird angepasst, um die Merkmalswichtigkeiten zu berechnen.
from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators=750, n_jobs=n_jobs, random_state=42)

forest.fit(X, y)
```
