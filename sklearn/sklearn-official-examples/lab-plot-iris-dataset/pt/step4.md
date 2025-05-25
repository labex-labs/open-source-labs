# Executar PCA

Executaremos a Análise de Componentes Principais (PCA) para reduzir a dimensionalidade do conjunto de dados. Projetamos os dados nos três primeiros componentes principais e plotamos os resultados em 3D.

```python
fig = plt.figure(1, figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d", elev=-150, azim=110)

X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    X_reduced[:, 2],
    c=y,
    cmap=plt.cm.Set1,
    edgecolor="k",
    s=40,
)

ax.set_title("Primeiras três direções PCA")
ax.set_xlabel("1º autovetor")
ax.xaxis.set_ticklabels([])
ax.set_ylabel("2º autovetor")
ax.yaxis.set_ticklabels([])
ax.set_zlabel("3º autovetor")
ax.zaxis.set_ticklabels([])
```
