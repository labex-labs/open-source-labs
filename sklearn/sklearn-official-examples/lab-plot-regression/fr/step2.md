# Ajuster le modèle de régression

Nous ajustons ensuite notre modèle de régression aux données d'échantillonnage en utilisant 5 voisins et des poids uniformes et basés sur la distance. Nous utilisons une boucle `for` pour itérer sur chaque type de poids et créer un nuage de points des points de données et un tracé de ligne des valeurs prédites en utilisant la méthode `predict` du modèle ajusté.

```python
n_neighbors = 5

for i, weights in enumerate(["uniform", "distance"]):
    knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
    y_ = knn.fit(X, y).predict(T)

    plt.subplot(2, 1, i + 1)
    plt.scatter(X, y, color="darkorange", label="données")
    plt.plot(T, y_, color="navy", label="prédiction")
    plt.axis("tight")
    plt.legend()
    plt.title("KNeighborsRegressor (k = %i, poids = '%s')" % (n_neighbors, weights))

plt.tight_layout()
plt.show()
```
