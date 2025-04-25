# 定义评估基准

我们将定义一个基准来比较 K 均值的不同初始化方法。我们的基准将：

- 创建一个管道，该管道将使用 `StandardScaler` 对数据进行缩放
- 训练并记录管道拟合的时间
- 通过不同指标测量所获得聚类的性能

```python
from time import time
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def bench_k_means(kmeans, name, data, labels):
    """评估 KMeans 初始化方法的基准。

    参数
    ----------
    kmeans : KMeans 实例
        一个已设置好初始化的 `KMeans` 实例。
    name : str
        赋予该策略的名称。它将用于在表格中展示结果。
    data : 形状为 (n_samples, n_features) 的 ndarray
        要聚类的数据。
    labels : 形状为 (n_samples,) 的 ndarray
        用于计算需要一些监督的聚类指标的标签。
    """
    t0 = time()
    estimator = make_pipeline(StandardScaler(), kmeans).fit(data)
    fit_time = time() - t0
    results = [name, fit_time, estimator[-1].inertia_]

    # 定义仅需要真实标签和估计器标签的指标
    clustering_metrics = [
        metrics.homogeneity_score,
        metrics.completeness_score,
        metrics.v_measure_score,
        metrics.adjusted_rand_score,
        metrics.adjusted_mutual_info_score,
    ]
    results += [m(labels, estimator[-1].labels_) for m in clustering_metrics]

    # 轮廓系数需要完整的数据集
    results += [
        metrics.silhouette_score(
            data,
            estimator[-1].labels_,
            metric="euclidean",
            sample_size=300,
        )
    ]

    # 展示结果
    formatter_result = (
        "{:9s}\t{:.3f}s\t{:.0f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}"
    )
    print(formatter_result.format(*results))
```
