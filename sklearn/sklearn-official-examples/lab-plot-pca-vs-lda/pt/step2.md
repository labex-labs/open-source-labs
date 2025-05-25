# Executar PCA

Em seguida, executaremos a Análise de Componentes Principais (PCA) no conjunto de dados para identificar a combinação de atributos que explicam a maior variação nos dados. Vamos representar graficamente as diferentes amostras nos dois primeiros componentes principais.

```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

# Percentagem de variância explicada para cada componente
print("Proporção da variância explicada (primeiros dois componentes): %s" % str(pca.explained_variance_ratio_))

plt.figure()
colors = ["navy", "turquoise", "darkorange"]
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=0.8, lw=lw, label=target_name)

plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("PCA do Conjunto de Dados Iris")
plt.show()
```
