# TSNE 임베딩 시각화

다양한 최근접 이웃 변환기를 사용하여 TSNE 임베딩을 시각화합니다. `transformers`는 세 가지 파이프라인 (`내부 NearestNeighbors를 사용한 TSNE`, `KNeighborsTransformer를 사용한 TSNE`, `NMSlibTransformer를 사용한 TSNE`) 을 포함하는 리스트로 정의합니다. 데이터셋과 변환기를 반복하며 TSNE 임베딩을 플롯합니다. 이는 여러 방법에서 유사해야 합니다. 마지막에 플롯을 표시합니다.

```python
transformers = [
    ("TSNE with internal NearestNeighbors", TSNE(metric=metric, **tsne_params)),
    (
        "TSNE with KNeighborsTransformer",
        make_pipeline(
            KNeighborsTransformer(
                n_neighbors=n_neighbors, mode="distance", metric=metric
            ),
            TSNE(metric="precomputed", **tsne_params),
        ),
    ),
    (
        "TSNE with NMSlibTransformer",
        make_pipeline(
            NMSlibTransformer(n_neighbors=n_neighbors, metric=metric),
            TSNE(metric="precomputed", **tsne_params),
        ),
    ),
]

nrows = len(datasets)
ncols = np.sum([1 for name, model in transformers if "TSNE" in name])
fig, axes = plt.subplots(
    nrows=nrows, ncols=ncols, squeeze=False, figsize=(5 * ncols, 4 * nrows)
)
axes = axes.ravel()
i_ax = 0

for dataset_name, (X, y) in datasets:
    msg = f"Benchmarking on {dataset_name}:"
    print(f"\n{msg}\n" + str("-" * len(msg)))

    for transformer_name, transformer in transformers:
        longest = np.max([len(name) for name, model in transformers])
        start = time.time()
        Xt = transformer.fit_transform(X)
        transform_duration = time.time() - start
        print(
            f"{transformer_name:<{longest}} {transform_duration:.3f} sec"
            " (fit_transform)"
        )

        # plot TSNE embedding which should be very similar across methods
        axes[i_ax].set_title(transformer_name + "\non " + dataset_name)
        axes[i_ax].scatter(
            Xt[:, 0],
            Xt[:, 1],
            c=y.astype(np.int32),
            alpha=0.2,
            cmap=plt.cm.viridis,
        )
        axes[i_ax].xaxis.set_major_formatter(NullFormatter())
        axes[i_ax].yaxis.set_major_formatter(NullFormatter())
        axes[i_ax].axis("tight")
        i_ax += 1

fig.tight_layout()
plt.show()
```
