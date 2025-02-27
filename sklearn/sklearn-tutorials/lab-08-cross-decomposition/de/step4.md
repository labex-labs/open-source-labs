# PLSCanonical

#### Anpassen des PLSCanonical-Modells

Als nächstes verwenden wir den `PLSCanonical`-Algorithmus, der die kanonische Korrelation zwischen zwei Matrizen findet. Dieser Algorithmus ist nützlich, wenn es Multikollinearität zwischen den Merkmalen gibt.

```python
plsc = PLSCanonical(n_components=2)
plsc.fit(X, Y)
```

#### Transformation der Daten

Wir können die ursprünglichen Daten mit dem angepassten Modell transformieren. Die transformierten Daten werden eine reduzierte Dimension haben.

```python
X_transformed = plsc.transform(X)
Y_transformed = plsc.transform(Y)
```
