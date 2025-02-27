# Führe die Hauptkomponentenanalyse (PCA) durch

Jetzt, nachdem wir den Datensatz visualisiert haben, führen wir die PCA auf ihm durch. Dazu verwenden wir die Funktion `PCA()` von scikit-learn. Wir setzen die Anzahl der Komponenten auf 3, da wir den Datensatz von 4 Dimensionen (4 Merkmale) auf 3 Dimensionen reduzieren möchten.

```python
pca = decomposition.PCA(n_components=3)
pca.fit(X)
X = pca.transform(X)
```
