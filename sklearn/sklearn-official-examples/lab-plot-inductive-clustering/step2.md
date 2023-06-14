# Train Clustering Algorithm

In this step, we will train a clustering algorithm on the generated training data and get the cluster labels. We will use `AgglomerativeClustering` from scikit-learn to train the algorithm with 3 clusters.

```python
clusterer = AgglomerativeClustering(n_clusters=3)
cluster_labels = clusterer.fit_predict(X)
```


