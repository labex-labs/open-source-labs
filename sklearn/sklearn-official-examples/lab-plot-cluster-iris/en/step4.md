# Apply K-Means Clustering

Now, we will apply the K-Means Clustering algorithm to our data. We will initialize the algorithm with 3 clusters and fit it to our data.

```python
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
```
