# 基准测试并绘制原子和批量预测延迟图

我们将使用Scikit-Learn的 `predict()` 方法来测量每个实例和整个输入的运行时预测。我们将使用 `benchmark_estimator()` 函数来测量原子和批量模式下的预测运行时。然后，我们将使用 `boxplot_runtimes()` 函数以箱线图的形式绘制预测延迟的分布。

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
        "Prediction Time per Instance - %s, %d feats."
        % (pred_type.capitalize(), configuration["n_features"])
    )
    ax1.set_ylabel("Prediction Time (us)")
    plt.show()

configuration = {
    "n_train": int(1e3),
    "n_test": int(1e2),
    "n_features": int(1e2),
    "estimators": [
        {
            "name": "线性模型",
            "instance": SGDRegressor(
                penalty="elasticnet", alpha=0.01, l1_ratio=0.25, tol=1e-4
            ),
            "complexity_label": "非零系数",
            "complexity_computer": lambda clf: np.count_nonzero(clf.coef_),
        },
        {
            "name": "随机森林",
            "instance": RandomForestRegressor(),
            "complexity_label": "估计器",
            "complexity_computer": lambda clf: clf.n_estimators,
        },
        {
            "name": "支持向量回归",
            "instance": SVR(kernel="rbf"),
            "complexity_label": "支持向量",
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
    stats[estimator_conf["name"]] = {"原子": a, "批量": b}
cls_names = [estimator_conf["name"] for estimator_conf in configuration["estimators"]]
runtimes = [1e6 * stats[clf_name]["原子"] for clf_name in cls_names]
boxplot_runtimes(runtimes, "原子", configuration)
runtimes = [1e6 * stats[clf_name]["批量"] for clf_name in cls_names]
boxplot_runtimes(runtimes, "批量 (%d)" % configuration["n_test"], configuration)
```
