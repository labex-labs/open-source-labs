# 특징 수의 예측 지연 시간에 미치는 영향 벤치마크

Scikit-Learn 의 `Ridge()` 추정기를 사용하여 특징 수가 예측 시간에 미치는 영향을 추정합니다. `n_feature_influence()` 함수를 사용하여 영향을 추정하고, `plot_n_features_influence()` 함수를 사용하여 특징 수에 따른 예측 시간의 변화를 플롯합니다.

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
