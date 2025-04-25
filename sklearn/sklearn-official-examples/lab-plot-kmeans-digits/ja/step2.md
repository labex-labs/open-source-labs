# 評価基準の定義

K - Means の異なる初期化方法を比較するための基準を定義します。私たちの基準は、以下のことを行います。

- `StandardScaler`を使ってデータをスケーリングするパイプラインを作成する
- パイプラインのフィッティングを学習し、その時間を計測する
- 異なる指標を使って得られたクラスタリングの性能を測定する

```python
from time import time
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def bench_k_means(kmeans, name, data, labels):
    """KMeans 初期化方法を評価するための基準。

    パラメータ
    ----------
    kmeans : KMeans インスタンス
        初期化が既に設定された `KMeans` インスタンス。
    name : str
        戦略に与えられた名前。表に結果を表示する際に使用されます。
    data : 形状 (n_samples, n_features) の ndarray
        クラスタリングするデータ。
    labels : 形状 (n_samples,) の ndarray
        ある程度の監視が必要なクラスタリング指標を計算する際に使用されるラベル。
    """
    t0 = time()
    estimator = make_pipeline(StandardScaler(), kmeans).fit(data)
    fit_time = time() - t0
    results = [name, fit_time, estimator[-1].inertia_]

    # 真のラベルと推定器のラベルのみが必要な指標を定義する
    clustering_metrics = [
        metrics.homogeneity_score,
        metrics.completeness_score,
        metrics.v_measure_score,
        metrics.adjusted_rand_score,
        metrics.adjusted_mutual_info_score,
    ]
    results += [m(labels, estimator[-1].labels_) for m in clustering_metrics]

    # シルエットスコアには完全なデータセットが必要
    results += [
        metrics.silhouette_score(
            data,
            estimator[-1].labels_,
            metric="euclidean",
            sample_size=300,
        )
    ]

    # 結果を表示する
    formatter_result = (
        "{:9s}\t{:.3f}s\t{:.0f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}"
    )
    print(formatter_result.format(*results))
```
