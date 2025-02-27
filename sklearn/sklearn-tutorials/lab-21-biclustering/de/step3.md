# Führen Sie das Spectral Biclustering durch

Als nächstes führen wir das Biclustering mit dem Spectral Biclustering-Algorithmus durch. Dieser Algorithmus geht davon aus, dass die Datenmatrix eine versteckte Schachbrettstruktur aufweist.

```python
# Initialisieren und anpassen des Spectral Biclustering-Modells
model_bi = SpectralBiclustering(n_clusters=(2, 3), random_state=0)
model_bi.fit(data)

# Holen Sie sich die Zeilen- und Spaltenclusterzugehörigkeit
row_clusters_bi = model_bi.row_labels_
column_clusters_bi = model_bi.column_labels_
```
