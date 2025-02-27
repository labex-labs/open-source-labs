# Hauptkomponentenanalyse (PCA) durchführen

Wir werden die PCA auf dem Iris-Datensatz durchführen, indem wir eine Instanz der PCA-Klasse initialisieren und sie auf die Daten anpassen.

```python
pca = PCA(n_components=n_components)
X_pca = pca.fit_transform(X)
```
