# Perform Spectral Biclustering

Next, let's perform biclustering using the Spectral Biclustering algorithm. This algorithm assumes that the data matrix has a hidden checkerboard structure.

```python
# Initialize and fit the Spectral Biclustering model
model_bi = SpectralBiclustering(n_clusters=(2, 3), random_state=0)
model_bi.fit(data)

# Get row and column cluster membership
row_clusters_bi = model_bi.row_labels_
column_clusters_bi = model_bi.column_labels_
```
