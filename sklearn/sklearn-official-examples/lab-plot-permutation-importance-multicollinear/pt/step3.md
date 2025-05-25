# Lidar com Características Multicolinear

Quando as características são colineares, a permutação de uma característica terá pouco efeito no desempenho do modelo, pois pode obter a mesma informação de uma característica correlacionada. Uma forma de lidar com características multicolinear é realizar agrupamento hierárquico nas correlações de posto de Spearman, escolher um limiar e manter uma única característica de cada cluster. Primeiro, plotamos um mapa de calor das características correlacionadas.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))
corr = spearmanr(X).correlation

# Garantir que a matriz de correlação seja simétrica
corr = (corr + corr.T) / 2
np.fill_diagonal(corr, 1)

# Convertemos a matriz de correlação em uma matriz de distância antes de realizar
# o agrupamento hierárquico usando o linkage de Ward.
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
