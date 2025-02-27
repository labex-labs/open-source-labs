# Solutions possibles

Nous allons discuter de quelques solutions possibles aux limitations de la classification par k-means. Dans le bloc de code suivant, nous montrons comment trouver le nombre correct de clusters pour le premier ensemble de données et comment traiter les grappes de tailles inégales en augmentant le nombre d'initialisations aléatoires.

```python
y_pred = KMeans(n_clusters=3, **common_params).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title("Optimal Number of Clusters")
plt.show()

y_pred = KMeans(n_clusters=3, n_init=10, random_state=random_state).fit_predict(
    X_filtered
)
plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
plt.title("Unevenly Sized Blobs \nwith several initializations")
plt.show()
```
