# Avaliação Quantitativa dos Métodos de Inicialização

Avaliaremos a capacidade das estratégias de inicialização do k-means em tornar a convergência do algoritmo robusta. Mediremos o desvio padrão relativo da inércia do agrupamento, que é a soma das distâncias quadradas aos centros de cluster mais próximos. O primeiro gráfico mostra a melhor inércia alcançada para cada combinação do modelo (`KMeans` ou `MiniBatchKMeans`) e do método de inicialização (`init="random"` ou `init="k-means++"`) para valores crescentes do parâmetro `n_init`, que controla o número de inicializações.

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
    print("Avaliação de %s com inicialização %s" % (factory.__name__, init))
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
    legends.append("%s com inicialização %s" % (factory.__name__, init))

plt.xlabel("n_init")
plt.ylabel("inércia")
plt.legend(plots, legends)
plt.title("Inércia média para diferentes inicializações k-means em %d execuções" % n_runs)
```
