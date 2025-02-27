# Effectuer l'ACP

Ensuite, nous effectuerons l'Analyse en Composantes Principales (ACP) sur l'ensemble de données pour identifier la combinaison d'attributs qui explique la plus grande partie de la variance des données. Nous tracerons les différents échantillons sur les deux premières composantes principales.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

# Taux de variance expliquée pour chaque composante
print("Explained variance ratio (first two components): %s" % str(pca.explained_variance_ratio_))

plt.figure()
colors = ["navy", "turquoise", "darkorange"]
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=0.8, lw=lw, label=target_name)

plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("PCA of Iris Dataset")
plt.show()
```
