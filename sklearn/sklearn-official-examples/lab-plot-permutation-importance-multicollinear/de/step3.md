# Multikollineare Features behandeln

Wenn Features kollinear sind, hat das Permutieren eines Features nur wenig Auswirkung auf die Modellleistung, da es die gleiche Information aus einem korrelierten Feature erhalten kann. Ein Möglichkeit, um multikollineare Features zu behandeln, besteht darin, eine hierarchische Clusteranalyse auf den Spearman-Rangkorrelationen durchzuführen, einen Schwellenwert auszuwählen und aus jeder Cluster nur ein einziges Feature zu behalten. Zunächst plotten wir eine Heatmap der korrelierten Features.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))
corr = spearmanr(X).correlation

# Stellen Sie sicher, dass die Korrelationsmatrix symmetrisch ist
corr = (corr + corr.T) / 2
np.fill_diagonal(corr, 1)

# Bevor wir die hierarchische Clusteranalyse mit Ward-Verknüpfung durchführen,
# konvertieren wir die Korrelationsmatrix in eine Distanzmatrix.
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
