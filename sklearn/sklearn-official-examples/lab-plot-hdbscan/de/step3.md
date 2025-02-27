# Mehrskalen-Clustering

Wir werden zeigen, dass HDBSCAN in der Lage ist, Mehrskalen-Clustering durchzuführen, was Cluster mit unterschiedlicher Dichte berücksichtigt. Traditionelles DBSCAN geht davon aus, dass alle potenziellen Cluster in ihrer Dichte homogen sind.

```python
centers = [[-0.85, -0.85], [-0.85, 0.85], [3, 3], [3, -3]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=[0.2, 0.35, 1.35, 1.35], random_state=0)

fig, axes = plt.subplots(2, 1, figsize=(10, 8))
params = {"eps": 0.7}
dbs = DBSCAN(**params).fit(X)
plot(X, dbs.labels_, parameters=params, ax=axes[0])
params = {"eps": 0.3}
dbs = DBSCAN(**params).fit(X)
plot(X, dbs.labels_, parameters=params, ax=axes[1])

hdb = HDBSCAN().fit(X)
plot(X, hdb.labels_, hdb.probabilities_)
```
