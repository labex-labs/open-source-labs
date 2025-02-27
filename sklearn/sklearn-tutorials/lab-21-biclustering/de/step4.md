# Visualisieren der Ergebnisse

Schließlich visualisieren wir die Biclusterstrukturen, die aus den Spectral Co-Clustering- und Spectral Biclustering-Algorithmen erhalten wurden.

```python
# Visualisierung für Spectral Co-Clustering
print("Spectral Co-Clustering:")
print("Zeilencluster:")
print(row_clusters_co)
print("Spaltencluster:")
print(column_clusters_co)

# Visualisierung für Spectral Biclustering
print("\nSpectral Biclustering:")
print("Zeilencluster:")
print(row_clusters_bi)
print("Spaltencluster:")
print(column_clusters_bi)
```
