# Um Recurso Informativo, um Cluster por Classe

Criamos um conjunto de dados com um recurso informativo e um cluster por classe, e o plotamos.

```python
plt.subplot(321)
plt.title("Um recurso informativo, um cluster por classe", fontsize="small")
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```
