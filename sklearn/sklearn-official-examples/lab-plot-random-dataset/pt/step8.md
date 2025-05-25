# Gaussiana Dividida em Três Quantis

Criamos um conjunto de dados com uma gaussiana dividida em três quantis e o plotamos.

```python
plt.subplot(326)
plt.title("Gaussiana dividida em três quantis", fontsize="small")
X1, Y1 = make_gaussian_quantiles(n_features=2, n_classes=3)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```
