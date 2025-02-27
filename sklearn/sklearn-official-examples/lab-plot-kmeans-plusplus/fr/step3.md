# Tracer les graines d'initialisation en même temps que les données d'échantillonnage

Nous allons utiliser la bibliothèque matplotlib pour tracer les graines d'initialisation en même temps que les données d'échantillonnage. Les graines d'initialisation seront représentées comme des points bleus, et les données d'échantillonnage seront représentées comme des points colorés.

```python
# Tracer les graines d'initialisation en même temps que les données d'échantillonnage
plt.figure(1)
colors = ["#4EACC5", "#FF9C34", "#4E9A06", "m"]

for k, col in enumerate(colors):
    cluster_data = y_true == k
    plt.scatter(X[cluster_data, 0], X[cluster_data, 1], c=col, marker=".", s=10)

plt.scatter(centers_init[:, 0], centers_init[:, 1], c="b", s=50)
plt.title("Initialisation K-Means++")
plt.xticks([])
plt.yticks([])
plt.show()
```
