# Gérer les fonctionnalités multicolinéaires

Lorsque les fonctionnalités sont colinéaires, permuter une fonctionnalité aura peu d'effet sur les performances du modèle car il peut obtenir les mêmes informations à partir d'une fonctionnalité corrélée. Une manière de gérer les fonctionnalités multicolinéaires consiste à effectuer une agrégation hiérarchique sur les corrélations de classement de Spearman, à choisir un seuil et à conserver une seule fonctionnalité de chaque groupe. Tout d'abord, nous traçons une carte thermique des fonctionnalités corrélées.

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
