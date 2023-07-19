# Perform Spectral Co-Clustering

Now, let's perform biclustering using the Spectral Co-Clustering algorithm. This algorithm finds biclusters with higher values compared to other rows and columns.

```python
# Initialize and fit the Spectral Co-Clustering model
model_co = SpectralCoclustering(n_clusters=3, random_state=0)
model_co.fit(data)

# Get row and column cluster membership
row_clusters_co = model_co.row_labels_
column_clusters_co = model_co.column_labels_
```
