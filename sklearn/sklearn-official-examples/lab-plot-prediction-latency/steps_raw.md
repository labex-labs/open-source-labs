# Prediction Latency with Scikit-Learn Estimators

## Introduction

The prediction latency of machine learning models is a crucial factor in real-world applications. In this lab, we will use Scikit-Learn estimators to benchmark the prediction latency of various regressors. We will measure the latency when doing predictions either in bulk or atomic mode. The plots will represent the distribution of the prediction latency as a boxplot.

## Steps

### Step 1: Generate a Regression Dataset

We will generate a regression dataset with the given parameters using Scikit-Learn's `make_regression` function. The dataset will have `n_train` training instances, `n_test` testing instances, `n_features` features, and `noise` of 0.1.

```python
X, y, coef = make_regression(
    n_samples=n_train + n_test, n_features=n_features, noise=noise, coef=True
)

random_seed = 13
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=n_train, test_size=n_test, random_state=random_seed
)
X_train, y_train = shuffle(X_train, y_train, random_state=random_seed)

X_scaler = StandardScaler()
X_train = X_scaler.fit_transform(X_train)
X_test = X_scaler.transform(X_test)

y_scaler = StandardScaler()
y_train = y_scaler.fit_transform(y_train[:, None])[:, 0]
y_test = y_scaler.transform(y_test[:, None])[:, 0]
```

### Step 2: Benchmark and Plot Atomic and Bulk Prediction Latency

We will use Scikit-Learn's `predict()` method to measure the runtime prediction of each instance and the whole input. We will use the `benchmark_estimator()` function to measure the runtimes of prediction in both atomic and bulk mode. Then, we will use the `boxplot_runtimes()` function to plot the distribution of the prediction latency as a boxplot.

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
            "name": "Linear Model",
            "instance": SGDRegressor(
                penalty="elasticnet", alpha=0.01, l1_ratio=0.25, tol=1e-4
            ),
            "complexity_label": "non-zero coefficients",
            "complexity_computer": lambda clf: np.count_nonzero(clf.coef_),
        },
        {
            "name": "RandomForest",
            "instance": RandomForestRegressor(),
            "complexity_label": "estimators",
            "complexity_computer": lambda clf: clf.n_estimators,
        },
        {
            "name": "SVR",
            "instance": SVR(kernel="rbf"),
            "complexity_label": "support vectors",
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
boxplot_runtimes(runtimes, "atomic", configuration)
runtimes = [1e6 * stats[clf_name]["bulk"] for clf_name in cls_names]
boxplot_runtimes(runtimes, "bulk (%d)" % configuration["n_test"], configuration)
```

### Step 3: Benchmark n_features Influence on Prediction Latency

We will use Scikit-Learn's `Ridge()` estimator to estimate the influence of the number of features on prediction time. We will use the `n_feature_influence()` function to estimate the influence, and the `plot_n_features_influence()` function to plot the evolution of prediction time with the number of features.

```python
def n_feature_influence(estimators, n_train, n_test, n_features, percentile):
    percentiles = defaultdict(defaultdict)
    for n in n_features:
        X_train, y_train, X_test, y_test = generate_dataset(n_train, n_test, n)
        for cls_name, estimator in estimators.items():
            estimator.fit(X_train, y_train)
            gc.collect()
            runtimes = bulk_benchmark_estimator(estimator, X_test, 30, False)
            percentiles[cls_name][n] = 1e6 * np.percentile(runtimes, percentile)
    return percentiles

def plot_n_features_influence(percentiles, percentile):
    fig, ax1 = plt.subplots(figsize=(10, 6))
    colors = ["r", "g", "b"]
    for i, cls_name in enumerate(percentiles.keys()):
        x = np.array(sorted([n for n in percentiles[cls_name].keys()]))
        y = np.array([percentiles[cls_name][n] for n in x])
        plt.plot(
            x,
            y,
            color=colors[i],
        )
    ax1.yaxis.grid(True, linestyle="-", which="major", color="lightgrey", alpha=0.5)
    ax1.set_axisbelow(True)
    ax1.set_title("Evolution of Prediction Time with #Features")
    ax1.set_xlabel("#Features")
    ax1.set_ylabel("Prediction Time at %d%%-ile (us)" % percentile)
    plt.show()

percentile = 90
percentiles = n_feature_influence(
    {"ridge": Ridge()},
    configuration["n_train"],
    configuration["n_test"],
    [100, 250, 500],
    percentile,
)
plot_n_features_influence(percentiles, percentile)
```

### Step 4: Benchmark Throughput

We will use Scikit-Learn's `predict()` method to measure the throughput for different estimators. We will use the `benchmark_throughputs()` function to benchmark the throughput, and the `plot_benchmark_throughput()` function to plot the prediction throughput for different estimators.

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
    ax.set_ylabel("Throughput (predictions/sec)")
    ax.set_title(
        "Prediction Throughput for different estimators (%d features)"
        % configuration["n_features"]
    )
    plt.show()

throughputs = benchmark_throughputs(configuration)
plot_benchmark_throughput(throughputs, configuration)
```

## Summary

In this lab, we learned how to use Scikit-Learn estimators to benchmark the prediction latency of various regressors. We measured the latency when doing predictions either in bulk or atomic mode, and we plotted the distribution of the prediction latency as a boxplot. We also estimated the influence of the number of features on prediction time and plotted the evolution of prediction time with the number of features. Lastly, we measured the throughput for different estimators and plotted the prediction throughput for different estimators.
