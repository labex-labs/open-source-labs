# PLSSVD

#### Anpassen des PLSSVD-Modells

Der `PLSSVD`-Algorithmus ist eine vereinfachte Version von `PLSCanonical`, der die Singulärwertzerlegung (SVD) der Kreuzkovarianzmatrix nur einmal berechnet. Dieser Algorithmus ist nützlich, wenn die Anzahl der Komponenten auf eins begrenzt ist.

```python
plssvd = PLSSVD(n_components=1)
plssvd.fit(X, Y)
```

#### Transformation der Daten

Wir können die ursprünglichen Daten mit dem angepassten Modell transformieren. Die transformierten Daten werden eine reduzierte Dimension haben.

```python
X_transformed = plssvd.transform(X)
Y_transformed = plssvd.transform(Y)
```
