# Sparse Zufallsprojektion

Als nächstes probieren wir eine andere Art von Zufallsprojektion, die als sparse Zufallsprojektion bezeichnet wird.

```python
transformer = random_projection.SparseRandomProjection()
X_new = transformer.fit_transform(X)
```

Hier erstellen wir eine Instanz der Klasse `SparseRandomProjection` und wenden sie auf unsere Daten `X` mit der Methode `fit_transform` an. Das Ergebnis wird in der Variable `X_new` gespeichert.
