# Führen Sie das Spectral Co-Clustering durch

Jetzt führen wir das Biclustering mit dem Spectral Co-Clustering-Algorithmus durch. Dieser Algorithmus findet Bicluster mit höheren Werten im Vergleich zu anderen Zeilen und Spalten.

```python
# Initialisieren und anpassen des Spectral Co-Clustering-Modells
model_co = SpectralCoclustering(n_clusters=3, random_state=0)
model_co.fit(data)

# Holen Sie sich die Zeilen- und Spaltenclusterzugehörigkeit
row_clusters_co = model_co.row_labels_
column_clusters_co = model_co.column_labels_
```
