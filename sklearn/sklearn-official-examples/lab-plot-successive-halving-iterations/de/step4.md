# Erstellen eines Objekts für die sukzessive Zufallssuche

Erstelle ein `HalvingRandomSearchCV`-Objekt, um durch den Parameterspace zu durchsuchen. Das Objekt nimmt die folgenden Argumente entgegen:

- `estimator`: der Optimierungsalgorithmus
- `param_distributions`: der Parameterspace, durch den gesucht werden soll
- `factor`: der Faktor, um den die Anzahl der Kandidaten in jeder Iteration reduziert wird
- `random_state`: der Zufallszustand, der für die Suche verwendet wird

Der Code zum Erstellen des Objekts lautet wie folgt:

```python
clf = RandomForestClassifier(n_estimators=20, random_state=rng)
rsh = HalvingRandomSearchCV(
    estimator=clf, param_distributions=param_dist, factor=2, random_state=rng
)
```
