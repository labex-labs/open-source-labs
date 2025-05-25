# Múltiplas Classes, Dois Recursos Informativos, um Cluster

Criamos um conjunto de dados com múltiplas classes, dois recursos informativos e um cluster, e o plotamos.

```python
plt.subplot(324)
plt.title("Múltiplas classes, dois recursos informativos, um cluster", fontsize="small")
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=2, n_clusters_per_class=1, n_classes=3)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```
