# Ajustar o Modelo de Regressão

Em seguida, ajustamos o nosso modelo de regressão aos dados de amostra utilizando 5 vizinhos e pesos uniformes e de distância. Usamos um loop `for` para iterar sobre cada tipo de peso e criar um gráfico de dispersão dos pontos de dados e um gráfico de linhas dos valores previstos usando o método `predict` do modelo ajustado.

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
