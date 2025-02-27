# CCA

#### Anpassen des CCA-Modells

Der `CCA`-Algorithmus ist ein spezieller Fall von PLS und steht für Canonical Correlation Analysis. Er findet die Korrelation zwischen zwei Mengen von Variablen.

```python
cca = CCA(n_components=2)
cca.fit(X, Y)
```

#### Transformation der Daten

Wir können die ursprünglichen Daten mit dem angepassten Modell transformieren. Die transformierten Daten werden eine reduzierte Dimension haben.

```python
X_transformed = cca.transform(X)
Y_transformed = cca.transform(Y)
```
