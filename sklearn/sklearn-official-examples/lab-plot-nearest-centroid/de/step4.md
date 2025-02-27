# Erstellen und Anpassen des Klassifiziers

Wir erstellen eine Instanz des Klassifiziers mit nächstem Zentrum (Nearest Centroid Classifier) mit einem Schrumpfwert (shrinkage value) von 0,2 und passen die Daten an.

```python
clf = NearestCentroid(shrink_threshold=0.2)
clf.fit(X, y)
```
