# 基准测试吞吐量

我们将使用Scikit-Learn的 `predict()` 方法来测量不同估计器的吞吐量。我们会使用 `benchmark_throughputs()` 函数来进行吞吐量的基准测试，并使用 `plot_benchmark_throughput()` 函数来绘制不同估计器的预测吞吐量。

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
    ax.set_ylabel("吞吐量 (预测次数/秒)")
    ax.set_title(
        "不同估计器的预测吞吐量 (%d 个特征)"
        % configuration["n_features"]
    )
    plt.show()

throughputs = benchmark_throughputs(configuration)
plot_benchmark_throughput(throughputs, configuration)
```
