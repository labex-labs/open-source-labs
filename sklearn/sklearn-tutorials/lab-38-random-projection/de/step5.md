# Inverse Transformation

Zufallsprojektionstransformatoren haben die Option, die Inverse der Projektionsmatrix zu berechnen. Lassen Sie uns diese Funktion erkunden, indem wir die inverse Transformation auf unsere projizierten Daten anwenden.

```python
transformer = random_projection.SparseRandomProjection(compute_inverse_components=True)
X_new = transformer.fit_transform(X)

# Compute the inverse transform
X_new_inversed = transformer.inverse_transform(X_new)
```

In diesem Schritt erstellen wir eine Instanz der Klasse `SparseRandomProjection` mit dem Parameter `compute_inverse_components` auf `True` gesetzt. Anschließend passen wir den Transformator auf unsere Daten `X` an und wenden die Transformation an. Schließlich berechnen wir die inverse Transformation, indem wir die Methode `inverse_transform` auf den projizierten Daten `X_new` aufrufen.
