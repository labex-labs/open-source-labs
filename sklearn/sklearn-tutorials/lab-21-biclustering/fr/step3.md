# Effectuez le biclustering spectral

Ensuite, effectuons le biclustering à l'aide de l'algorithme de biclustering spectral. Cet algorithme suppose que la matrice de données a une structure d'échiquier cachée.

```python
# Initialisez et ajustez le modèle de biclustering spectral
model_bi = SpectralBiclustering(n_clusters=(2, 3), random_state=0)
model_bi.fit(data)

# Obtenez la appartenance aux clusters de lignes et de colonnes
row_clusters_bi = model_bi.row_labels_
column_clusters_bi = model_bi.column_labels_
```
