# Regressionmodell anpassen

Wir passen dann unser Regressionsmodell an die Beispiel-Daten an, indem wir 5 Nachbarn und sowohl gleichmäßige als auch Abstandsgewichte verwenden. Wir verwenden eine for-Schleife, um über jeden Gewichtstyp zu iterieren, und erstellen einen Streudiagramm der Datensätze und einen Liniendiagramm der vorhergesagten Werte mithilfe der `predict`-Methode des angepassten Modells.

```python
n_neighbors = 5

for i, weights in enumerate(["uniform", "distance"]):
    knn = neighbors.KNeighborsRegressor(n_neighbors, weights=weights)
    y_ = knn.fit(X, y).predict(T)

    plt.subplot(2, 1, i + 1)
    plt.scatter(X, y, color="darkorange", label="data")
    plt.plot(T, y_, color="navy", label="prediction")
    plt.axis("tight")
    plt.legend()
    plt.title("KNeighborsRegressor (k = %i, weights = '%s')" % (n_neighbors, weights))

plt.tight_layout()
plt.show()
```
