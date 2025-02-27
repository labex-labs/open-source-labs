# マルチスケールクラスタリング

HDBSCAN が密度の異なるクラスタを含むマルチスケールクラスタリングが可能であることを示します。従来の DBSCAN は、潜在的なクラスタが密度が均一であると仮定しています。

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
