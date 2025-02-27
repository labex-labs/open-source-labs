# Ajustar el modelo de regresión

Luego ajustamos nuestro modelo de regresión a los datos de muestra utilizando 5 vecinos y pesos uniformes y de distancia. Utilizamos un bucle `for` para iterar sobre cada tipo de peso y crear un diagrama de dispersión de los puntos de datos y un diagrama de líneas de los valores predichos utilizando el método `predict` del modelo ajustado.

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
