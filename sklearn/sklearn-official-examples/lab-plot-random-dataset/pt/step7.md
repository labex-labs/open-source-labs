# Três Blobs

Criamos um conjunto de dados com três blobs e o plotamos.

```python
plt.subplot(325)
plt.title("Três blobs", fontsize="small")
X1, Y1 = make_blobs(n_features=2, centers=3)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```
