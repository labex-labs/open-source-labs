# Gaußsche Zufallsprojektion

Nun wenden wir die Gaußsche Zufallsprojektion an, um die Dimension unserer Daten zu reduzieren.

```python
transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
```

In diesem Schritt erstellen wir eine Instanz der Klasse `GaussianRandomProjection` und passen sie auf unsere Daten `X` an. Anschließend wenden wir die Transformation an, indem wir die Methode `fit_transform` aufrufen. Das Ergebnis wird in der Variable `X_new` gespeichert.
