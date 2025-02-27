# Hauptkomponentenanalyse (PCA) durchführen

Als nächstes werden wir die PCA auf unserem Datensatz durchführen. Zunächst verbinden wir `x`, `y` und `z`, um ein 3D-Array `Y` zu bilden. Anschließend erstellen wir eine Instanz der PCA-Klasse und passen sie an unsere Daten an. Anschließend können wir die Hauptkomponenten über das Attribut `components_` des PCA-Objekts zugreifen.

```python
Y = np.c_[x, y, z]
pca = PCA(n_components=3)
pca.fit(Y)
components = pca.components_
```
