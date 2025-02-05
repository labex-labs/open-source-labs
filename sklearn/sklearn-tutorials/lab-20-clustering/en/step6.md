# Evaluate the Clustering

To evaluate the clustering results, we can calculate the inertia of the clusters, which represents the sum of squared distances of samples to their closest cluster center.

```python
# Calculate the inertia of the clusters
inertia = kmeans.inertia_
print("Inertia:", inertia)
```
