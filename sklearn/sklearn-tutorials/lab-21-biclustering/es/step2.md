# Realizar Co-Clustering Espectral

Ahora, realicemos el biclustering utilizando el algoritmo de Co-Clustering Espectral. Este algoritmo encuentra biclusters con valores más altos en comparación con otras filas y columnas.

```python
# Inicializar y ajustar el modelo de Co-Clustering Espectral
model_co = SpectralCoclustering(n_clusters=3, random_state=0)
model_co.fit(data)

# Obtener la pertenencia de los clusters de filas y columnas
row_clusters_co = model_co.row_labels_
column_clusters_co = model_co.column_labels_
```
