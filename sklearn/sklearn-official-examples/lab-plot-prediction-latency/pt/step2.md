# Avaliar e Representar Graficamente a Latência de Previsão Atómica e em Massa

Usaremos o método `predict()` do Scikit-Learn para medir o tempo de execução da previsão de cada instância e de toda a entrada. Usaremos a função `benchmark_estimator()` para medir os tempos de execução da previsão em modo atómico e em massa. Em seguida, usaremos a função `boxplot_runtimes()` para representar graficamente a distribuição da latência de previsão como um boxplot.

```python
def benchmark_estimator(estimator, X_test, n_bulk_repeats=30, verbose=False):
    atomic_runtimes = atomic_benchmark_estimator(estimator, X_test, verbose)
    bulk_runtimes = bulk_benchmark_estimator(estimator, X_test, n_bulk_repeats, verbose)
    return atomic_runtimes, bulk_runtimes

def boxplot_runtimes(runtimes, pred_type, configuration):
    fig, ax1 = plt.subplots(figsize=(10, 6))
    bp = plt.boxplot(
        runtimes,
    )
    cls_infos = [
        "%s\n(%d %s)"
        % (
            estimator_conf["name"],
            estimator_conf["complexity_computer"](estimator_conf["instance"]),
            estimator_conf["complexity_label"],
        )
        for estimator_conf in configuration["estimators"]
    ]
    plt.setp(ax1, xticklabels=cls_infos)
    plt.setp(bp["boxes"], color="black")
    plt.setp(bp["whiskers"], color="black")
    plt.setp(bp["fliers"], color="red", marker="+")
    ax1.yaxis.grid(True, linestyle="-", which="major", color="lightgrey", alpha=0.5)
    ax1.set_axisbelow(True)
    ax1.set_title(
        "Tempo de Previsão por Instância - %s, %d características."
        % (pred_type.capitalize(), configuration["n_features"])
    )
    ax1.set_ylabel("Tempo de Previsão (us)")
    plt.show()

configuration = {
    "n_train": int(1e3),
    "n_test": int(1e2),
    "n_features": int(1e2),
    "estimators": [
        {
            "name": "Modelo Linear",
            "instance": SGDRegressor(
                penalty="elasticnet", alpha=0.01, l1_ratio=0.25, tol=1e-4
            ),
            "complexity_label": "coeficientes não nulos",
            "complexity_computer": lambda clf: np.count_nonzero(clf.coef_),
        },
        {
            "name": "RandomForest",
            "instance": RandomForestRegressor(),
            "complexity_label": "estimadores",
            "complexity_computer": lambda clf: clf.n_estimators,
        },
        {
            "name": "SVR",
            "instance": SVR(kernel="rbf"),
            "complexity_label": "vetores de suporte",
            "complexity_computer": lambda clf: len(clf.support_vectors_),
        },
    ],
}
X_train, y_train, X_test, y_test = generate_dataset(
    configuration["n_train"], configuration["n_test"], configuration["n_features"]
)
stats = {}
for estimator_conf in configuration["estimators"]:
    estimator_conf["instance"].fit(X_train, y_train)
    gc.collect()
    a, b = benchmark_estimator(estimator_conf["instance"], X_test)
    stats[estimator_conf["name"]] = {"atomic": a, "bulk": b}
cls_names = [estimator_conf["name"] for estimator_conf in configuration["estimators"]]
runtimes = [1e6 * stats[clf_name]["atomic"] for clf_name in cls_names]
boxplot_runtimes(runtimes, "atómico", configuration)
runtimes = [1e6 * stats[clf_name]["bulk"] for clf_name in cls_names]
boxplot_runtimes(runtimes, "em massa (%d)" % configuration["n_test"], configuration)
```
