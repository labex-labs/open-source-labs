# Realizar Biclustering Espectral

A continuación, realicemos el biclustering utilizando el algoritmo de Biclustering Espectral. Este algoritmo asume que la matriz de datos tiene una estructura de tablero de ajedrez oculta.

```python
# Inicializar y ajustar el modelo de Biclustering Espectral
model_bi = SpectralBiclustering(n_clusters=(2, 3), random_state=0)
model_bi.fit(data)

# Obtener la pertenencia de los clusters de filas y columnas
row_clusters_bi = model_bi.row_labels_
column_clusters_bi = model_bi.column_labels_
```
