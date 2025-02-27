# Nuage de points de données originales et réduites

Dans cette étape, nous allons créer un nuage de points de données originales et réduites.

```python
fig = plt.figure(figsize=(9, 8))

ax = plt.subplot(221)
ax.scatter(X[:, 0], X[:, 1], c=y, s=50, edgecolor="k")
ax.set_title("Données originales (2d)")
ax.set_xticks(())
ax.set_yticks(())

ax = plt.subplot(222)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, s=50, edgecolor="k")
ax.set_title(
    "Réduction par Truncated SVD (2d) des données transformées (%dd)" % X_transformed.shape[1]
)
ax.set_xticks(())
ax.set_yticks(())
```
