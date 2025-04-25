# 多重共線性を持つ特徴量を処理する

特徴量が共線的な場合、ある特徴量を入れ替えるとモデルの性能にほとんど影響がないことがあります。なぜなら、相関する特徴量から同じ情報を得ることができるからです。多重共線性を持つ特徴量を処理する方法の 1 つは、スピアマンの順位相関係数に基づいて階層的クラスタリングを行い、閾値を選び、各クラスタから 1 つの特徴量のみを残すことです。まず、相関する特徴量のヒートマップをプロットします。

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))
corr = spearmanr(X).correlation

# Ensure the correlation matrix is symmetric
corr = (corr + corr.T) / 2
np.fill_diagonal(corr, 1)

# We convert the correlation matrix to a distance matrix before performing
# hierarchical clustering using Ward's linkage.
distance_matrix = 1 - np.abs(corr)
dist_linkage = hierarchy.ward(squareform(distance_matrix))
dendro = hierarchy.dendrogram(
    dist_linkage, labels=data.feature_names.tolist(), ax=ax1, leaf_rotation=90
)
dendro_idx = np.arange(0, len(dendro["ivl"]))

ax2.imshow(corr[dendro["leaves"], :][:, dendro["leaves"]])
ax2.set_xticks(dendro_idx)
ax2.set_yticks(dendro_idx)
ax2.set_xticklabels(dendro["ivl"], rotation="vertical")
ax2.set_yticklabels(dendro["ivl"])
fig.tight_layout()
plt.show()
```
