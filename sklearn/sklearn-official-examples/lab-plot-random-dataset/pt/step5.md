# Dois Recursos Informativos, Dois Clusters por Classe

Criamos um conjunto de dados com dois recursos informativos e dois clusters por classe, e o plotamos.

```python
plt.subplot(323)
plt.title("Dois recursos informativos, dois clusters por classe", fontsize="small")
X2, Y2 = make_classification(n_features=2, n_redundant=0, n_informative=2)
plt.scatter(X2[:, 0], X2[:, 1], marker="o", c=Y2, s=25, edgecolor="k")
```
