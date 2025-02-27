# 実験2 - クラス数とクラスタ数を変化させる

このセクションでは、2つの一様に分布するランダムなラベリングに対していくつかのメトリックを使ってスコア付けする同様の関数を定義します。この場合、`n_clusters_range` の各可能な値に対して、クラス数と割り当てられたクラスタ数を一致させます。

```python
def uniform_labelings_scores(score_func, n_samples, n_clusters_range, n_runs=5):
    scores = np.zeros((len(n_clusters_range), n_runs))

    for i, n_clusters in enumerate(n_clusters_range):
        for j in range(n_runs):
            labels_a = random_labels(n_samples=n_samples, n_classes=n_clusters)
            labels_b = random_labels(n_samples=n_samples, n_classes=n_clusters)
            scores[i, j] = score_func(labels_a, labels_b)
    return scores
```
