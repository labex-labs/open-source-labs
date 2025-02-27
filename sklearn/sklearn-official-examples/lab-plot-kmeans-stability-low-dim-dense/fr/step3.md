# Evaluation quantitative des méthodes d'initialisation

Nous allons évaluer la capacité des stratégies d'initialisation de k-means à rendre la convergence de l'algorithme robuste. Nous allons mesurer l'écart-type relatif de l'inertie du clustering, qui est la somme des distances au carré au centre du cluster le plus proche. La première figure montre la meilleure inertie atteinte pour chaque combinaison du modèle (`KMeans` ou `MiniBatchKMeans`) et de la méthode d'initialisation (`init="random"` ou `init="k-means++"`) pour des valeurs croissantes du paramètre `n_init` qui contrôle le nombre d'initialisations.

```python
n_runs = 5
n_init_range = np.array([1, 5, 10, 15, 20])

plt.figure()
plots = []
legends = []

cases = [
    (KMeans, "k-means++", {}, "^-"),
    (KMeans, "random", {}, "o-"),
    (MiniBatchKMeans, "k-means++", {"max_no_improvement": 3}, "x-"),
    (MiniBatchKMeans, "random", {"max_no_improvement": 3, "init_size": 500}, "d-"),
]

for factory, init, params, format in cases:
    print("Evaluation of %s with %s init" % (factory.__name__, init))
    inertia = np.empty((len(n_init_range), n_runs))

    for run_id in range(n_runs):
        X, y = make_data(run_id, n_samples_per_center, grid_size, scale)
        for i, n_init in enumerate(n_init_range):
            km = factory(
                n_clusters=n_clusters,
                init=init,
                random_state=run_id,
                n_init=n_init,
                **params,
            ).fit(X)
            inertia[i, run_id] = km.inertia_
    p = plt.errorbar(
        n_init_range, inertia.mean(axis=1), inertia.std(axis=1), fmt=format
    )
    plots.append(p[0])
    legends.append("%s with %s init" % (factory.__name__, init))

plt.xlabel("n_init")
plt.ylabel("inertia")
plt.legend(plots, legends)
plt.title("Mean inertia for various k-means init across %d runs" % n_runs)
```
