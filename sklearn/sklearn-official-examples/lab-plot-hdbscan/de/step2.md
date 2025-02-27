# Skaleninvarianz

Wir werden zeigen, dass HDBSCAN im Gegensatz zu DBSCAN skaleninvariant ist. DBSCAN erfordert, dass der Parameter `eps` für den spezifischen zu verwendenden Datensatz eingestellt wird. Wir werden die Clusterung vergleichen, die mit dem gleichen Wert erhalten wird, aber auf skalierten Versionen des Datensatzes angewendet wird.

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
