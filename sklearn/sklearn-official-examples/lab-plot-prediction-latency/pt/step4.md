# Avaliação de Taxa de Processamento

Usaremos o método `predict()` do Scikit-Learn para medir a taxa de processamento para diferentes estimadores. Usaremos a função `benchmark_throughputs()` para avaliar a taxa de processamento e a função `plot_benchmark_throughput()` para representar graficamente a taxa de processamento de previsão para diferentes estimadores.

```python
def benchmark_throughputs(configuration, duration_secs=0.1):
    X_train, y_train, X_test, y_test = generate_dataset(
        configuration["n_train"], configuration["n_test"], configuration["n_features"]
    )
    throughputs = dict()
    for estimator_config in configuration["estimators"]:
        estimator_config["instance"].fit(X_train, y_train)
        start_time = time.time()
        n_predictions = 0
        while (time.time() - start_time) < duration_secs:
            estimator_config["instance"].predict(X_test[[0]])
            n_predictions += 1
        throughputs[estimator_config["name"]] = n_predictions / duration_secs
    return throughputs

def plot_benchmark_throughput(throughputs, configuration):
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = ["r", "g", "b"]
    cls_infos = [
        "%s\n(%d %s)"
        % (
            estimator_conf["name"],
            estimator_conf["complexity_computer"](estimator_conf["instance"]),
            estimator_conf["complexity_label"],
        )
        for estimator_conf in configuration["estimators"]
    ]
    cls_values = [
        throughputs[estimator_conf["name"]]
        for estimator_conf in configuration["estimators"]
    ]
    plt.bar(range(len(throughputs)), cls_values, width=0.5, color=colors)
    ax.set_xticks(np.linspace(0.25, len(throughputs) - 0.75, len(throughputs)))
    ax.set_xticklabels(cls_infos, fontsize=10)
    ymax = max(cls_values) * 1.2
    ax.set_ylim((0, ymax))
    ax.set_ylabel("Taxa de Processamento (previsões/seg)")
    ax.set_title(
        "Taxa de Processamento de Previsão para diferentes estimadores (%d características)"
        % configuration["n_features"]
    )
    plt.show()

throughputs = benchmark_throughputs(configuration)
plot_benchmark_throughput(throughputs, configuration)
```
