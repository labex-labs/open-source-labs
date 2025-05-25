# Modelo BIRCH

O terceiro passo é calcular o agrupamento com BIRCH com e sem a etapa de agrupamento final e plotar os resultados. Criaremos dois modelos BIRCH, um sem a etapa de agrupamento global e outro com a etapa de agrupamento global.

```python
# Calcular o agrupamento com BIRCH com e sem a etapa de agrupamento final e plotar.
birch_models = [
    Birch(threshold=1.7, n_clusters=None),
    Birch(threshold=1.7, n_clusters=100),
]
final_step = ["sem agrupamento global", "com agrupamento global"]

for ind, (birch_model, info) in enumerate(zip(birch_models, final_step)):
    t = time()
    birch_model.fit(X)
    print("BIRCH %s como etapa final levou %0.2f segundos" % (info, (time() - t)))

    # Plotar o resultado
    labels = birch_model.labels_
    centroids = birch_model.subcluster_centers_
    n_clusters = np.unique(labels).size
    print("n_clusters : %d" % n_clusters)

    ax = fig.add_subplot(1, 3, ind + 1)
    for this_centroid, k, col in zip(centroids, range(n_clusters), colors_):
        mask = labels == k
        ax.scatter(X[mask, 0], X[mask, 1], c="w", edgecolor=col, marker=".", alpha=0.5)
        if birch_model.n_clusters is None:
            ax.scatter(this_centroid[0], this_centroid[1], marker="+", c="k", s=25)
    ax.set_ylim([-25, 25])
    ax.set_xlim([-25, 25])
    ax.set_autoscaley_on(False)
    ax.set_title("BIRCH %s" % info)
```
