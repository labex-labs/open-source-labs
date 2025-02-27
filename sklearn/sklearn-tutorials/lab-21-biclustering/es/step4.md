# Visualizar los resultados

Finalmente, visualicemos las estructuras de biclusters obtenidas a partir de los algoritmos de Co-Clustering Espectral y Biclustering Espectral.

```python
# Visualización para Co-Clustering Espectral
print("Co-Clustering Espectral:")
print("Clusters de filas:")
print(row_clusters_co)
print("Clusters de columnas:")
print(column_clusters_co)

# Visualización para Biclustering Espectral
print("\nBiclustering Espectral:")
print("Clusters de filas:")
print(row_clusters_bi)
print("Clusters de columnas:")
print(column_clusters_bi)
```
