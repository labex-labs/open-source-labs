# 对不同的最近邻变换器进行基准测试

我们对不同的精确/近似最近邻变换器进行基准测试。我们定义数据集、变换器和参数，包括 `n_iter`、`perplexity`、`metric` 和 `n_neighbors`。我们测量每个变换器在每个数据集上进行拟合和变换所需的时间。我们打印出每个变换器进行拟合和变换所花费的时间。

```python
datasets = [
    ("MNIST_10000", load_mnist(n_samples=10_000)),
    ("MNIST_20000", load_mnist(n_samples=20_000)),
]

n_iter = 500
perplexity = 30
metric = "euclidean"
n_neighbors = int(3.0 * perplexity + 1) + 1

tsne_params = dict(
    init="random",  # pca not supported for sparse matrices
    perplexity=perplexity,
    method="barnes_hut",
    random_state=42,
    n_iter=n_iter,
    learning_rate="auto",
)

transformers = [
    (
        "KNeighborsTransformer",
        KNeighborsTransformer(n_neighbors=n_neighbors, mode="distance", metric=metric),
    ),
    (
        "NMSlibTransformer",
        NMSlibTransformer(n_neighbors=n_neighbors, metric=metric),
    ),
    (
        "PyNNDescentTransformer",
        PyNNDescentTransformer(
            n_neighbors=n_neighbors, metric=metric, parallel_batch_queries=True
        ),
    ),
]

for dataset_name, (X, y) in datasets:
    msg = f"Benchmarking on {dataset_name}:"
    print(f"\n{msg}\n" + str("-" * len(msg)))

    for transformer_name, transformer in transformers:
        longest = np.max([len(name) for name, model in transformers])
        start = time.time()
        transformer.fit(X)
        fit_duration = time.time() - start
        print(f"{transformer_name:<{longest}} {fit_duration:.3f} sec (fit)")
        start = time.time()
        Xt = transformer.transform(X)
        transform_duration = time.time() - start
        print(f"{transformer_name:<{longest}} {transform_duration:.3f} sec (transform)")
        if transformer_name == "PyNNDescentTransformer":
            start = time.time()
            Xt = transformer.transform(X)
            transform_duration = time.time() - start
            print(
                f"{transformer_name:<{longest}} {transform_duration:.3f} sec"
                " (transform)"
            )
```
