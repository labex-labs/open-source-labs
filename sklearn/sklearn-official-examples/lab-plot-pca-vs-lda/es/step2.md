# Realizar PCA

A continuación, realizaremos el Análisis de Componentes Principales (PCA, por sus siglas en inglés) en el conjunto de datos para identificar la combinación de atributos que explica la mayor varianza en los datos. Graficaremos las diferentes muestras en los primeros dos componentes principales.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

# Porcentaje de varianza explicada para cada componente
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
