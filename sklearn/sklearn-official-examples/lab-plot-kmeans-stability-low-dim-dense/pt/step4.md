# Inspeção Visual Qualitativa da Convergência

Demonstraremos uma única execução do estimador `MiniBatchKMeans` usando `init="random"` e `n_init=1`. Essa execução leva a uma má convergência (ótimo local), com os centros estimados presos entre os clusters verdadeiros.

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
        "Exemplo de alocação de clusters com uma única inicialização aleatória\ncom MiniBatchKMeans"
    )

plt.show()
```
