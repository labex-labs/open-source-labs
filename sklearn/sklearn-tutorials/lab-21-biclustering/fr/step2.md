# Effectuez le co-clustering spectral

Maintenant, effectuons le biclustering à l'aide de l'algorithme de co-clustering spectral. Cet algorithme trouve des biclusters avec des valeurs plus élevées par rapport à d'autres lignes et colonnes.

```python
# Initialisez et ajustez le modèle de co-clustering spectral
model_co = SpectralCoclustering(n_clusters=3, random_state=0)
model_co.fit(data)

# Obtenez la appartenance aux clusters de lignes et de colonnes
row_clusters_co = model_co.row_labels_
column_clusters_co = model_co.column_labels_
```
