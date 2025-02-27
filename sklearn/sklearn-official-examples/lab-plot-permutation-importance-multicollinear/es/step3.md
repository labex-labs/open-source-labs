# Manejar características multicolineales

Cuando las características son colineales, la permutación de una característica tendrá poco efecto en el rendimiento del modelo porque puede obtener la misma información de una característica correlacionada. Una forma de manejar las características multicolineales es realizando un clustering jerárquico en las correlaciones de rango de Spearman, elegir un umbral y mantener una sola característica de cada cluster. Primero, graficamos un mapa de calor de las características correlacionadas.

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))
corr = spearmanr(X).correlation

# Asegurarse de que la matriz de correlación sea simétrica
corr = (corr + corr.T) / 2
np.fill_diagonal(corr, 1)

# Convertimos la matriz de correlación a una matriz de distancias antes de realizar
# el clustering jerárquico utilizando el enlace de Ward.
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
