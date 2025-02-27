# 実験1 - 固定された正解ラベルとクラスタ数の増加

一様に分布するランダムなラベリングを作成し、`random_labels`関数を使用して、`n_classes`に分布する固定された正解ラベルのセット (`labels_a`) を作成し、次に、与えられた`n_clusters`での特定のメトリックの変動性を評価するために、いくつかのランダムに「予測」されたラベルのセット (`labels_b`) にスコアを付けます。

```python
rng = np.random.RandomState(0)

def random_labels(n_samples, n_classes):
    return rng.randint(low=0, high=n_classes, size=n_samples)

def fixed_classes_uniform_labelings_scores(
    score_func, n_samples, n_clusters_range, n_classes, n_runs=5
):
    scores = np.zeros((len(n_clusters_range), n_runs))
    labels_a = random_labels(n_samples=n_samples, n_classes=n_classes)

    for i, n_clusters in enumerate(n_clusters_range):
        for j in range(n_runs):
            labels_b = random_labels(n_samples=n_samples, n_classes=n_clusters)
            scores[i, j] = score_func(labels_a, labels_b)
    return scores
```
