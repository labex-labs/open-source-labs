# Invariance à l'échelle

Nous allons démontrer que HDBSCAN est invariant à l'échelle, contrairement à DBSCAN. DBSCAN nécessite que le paramètre `eps` soit ajusté pour le jeu de données spécifique utilisé. Nous allons comparer les regroupements obtenus avec la même valeur mais appliquée à des versions redimensionnées du jeu de données.

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
