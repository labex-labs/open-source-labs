# Qualitative Visual Inspection of the Convergence

Wir werden einen einzelnen Durchlauf des `MiniBatchKMeans`-Schätzers mit `init="random"` und `n_init=1` demonstrieren. Dieser Durchlauf führt zu einer schlechten Konvergenz (lokales Optimum), wobei die geschätzten Zentren zwischen den wahren Clustern stecken bleiben.

```python
km = MiniBatchKMeans(
    n_clusters=n_clusters, init="random", n_init=1, random_state=random_state
).fit(X)

plt.figure()
for k in range(n_clusters):
    my_members = km.labels_ == k
    color = cm.nipy_spectral(float(k) / n_clusters, 1)
    plt.plot(X[my_members, 0], X[my_members, 1], ".", c=color)
    cluster_center = km.cluster_centers_[k]
    plt.plot(
        cluster_center[0],
        cluster_center[1],
        "o",
        markerfacecolor=color,
        markeredgecolor="k",
        markersize=6,
    )
    plt.title(
        "Example cluster allocation with a single random init\nwith MiniBatchKMeans"
    )

plt.show()
```
