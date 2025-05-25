# 다중 스케일 군집화

HDBSCAN 이 다양한 밀도를 가진 클러스터를 고려하는 다중 스케일 군집화를 수행할 수 있는 것을 보여줍니다. 기존의 DBSCAN 은 모든 잠재적 클러스터가 균일한 밀도를 가진다고 가정합니다.

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
