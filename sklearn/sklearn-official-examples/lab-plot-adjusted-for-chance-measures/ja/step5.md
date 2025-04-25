# 実験 2 の結果をプロットする

`matplotlib` ライブラリを使って、第 2 の実験の結果をプロットします。第 1 の実験と同様の結果が観察されます：偶然に対する調整済みメトリックは一定でゼロに近く、他のメトリックは細かい粒度のラベリングで大きくなる傾向があります。ランダムなラベリングの平均 V-measure は、クラスタ数が測定に使用されたサンプルの総数に近づくにつれて大幅に増加します。

```python
n_samples = 100
n_clusters_range = np.linspace(2, n_samples, 10).astype(int)

plt.figure(2)

plots = []
names = []

for marker, (score_name, score_func) in zip("d^vx.,", score_funcs):
    scores = uniform_labelings_scores(score_func, n_samples, n_clusters_range)
    plots.append(
        plt.errorbar(
            n_clusters_range,
            np.median(scores, axis=1),
            scores.std(axis=1),
            alpha=0.8,
            linewidth=2,
            marker=marker,
        )[0]
    )
    names.append(score_name)

plt.title(
    "Clustering measures for 2 random uniform labelings\nwith equal number of clusters"
)
plt.xlabel(f"Number of clusters (Number of samples is fixed to {n_samples})")
plt.ylabel("Score value")
plt.legend(plots, names)
plt.ylim(bottom=-0.05, top=1.05)
plt.show()
```
