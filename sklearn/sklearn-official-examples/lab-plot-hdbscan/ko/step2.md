# 스케일 불변성

HDBSCAN 이 DBSCAN 과 달리 스케일 불변성을 갖는 것을 보여줍니다. DBSCAN 은 사용하는 특정 데이터 세트에 대해 `eps` 매개변수를 조정해야 합니다. 데이터 세트의 크기를 조정한 버전에 동일한 값을 적용하여 얻은 군집화를 비교합니다.

```python
fig, axes = plt.subplots(3, 1, figsize=(10, 12))
dbs = DBSCAN(eps=0.3)
for idx, scale in enumerate((1, 0.5, 3)):
    dbs.fit(X * scale)
    plot(X * scale, dbs.labels_, parameters={"scale": scale, "eps": 0.3}, ax=axes[idx])

fig, axis = plt.subplots(1, 1, figsize=(12, 5))
dbs = DBSCAN(eps=0.9).fit(3 * X)
plot(3 * X, dbs.labels_, parameters={"scale": 3, "eps": 0.9}, ax=axis)

fig, axes = plt.subplots(3, 1, figsize=(10, 12))
hdb = HDBSCAN()
for idx, scale in enumerate((1, 0.5, 3)):
    hdb.fit(X)
    plot(X, hdb.labels_, hdb.probabilities_, ax=axes[idx], parameters={"scale": scale})
```
