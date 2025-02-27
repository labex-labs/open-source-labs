# Visualisez les résultats

Enfin, visualisons les structures de biclusters obtenues à partir des algorithmes de co-clustering spectral et de biclustering spectral.

```python
# Visualisation pour le co-clustering spectral
print("Co-clustering spectral :")
print("Clusters de lignes :")
print(row_clusters_co)
print("Clusters de colonnes :")
print(column_clusters_co)

# Visualisation pour le biclustering spectral
print("\nBiclustering spectral :")
print("Clusters de lignes :")
print(row_clusters_bi)
print("Clusters de colonnes :")
print(column_clusters_bi)
```
