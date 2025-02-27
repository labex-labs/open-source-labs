# Настройка модели регрессии

Затем настраиваем нашу модель регрессии на выборочные данные, используя 5 соседей и веса, равномерные и зависящие от расстояния. Мы используем цикл for для перебора каждого типа весов и создаем точечную диаграмму данных и линейную диаграмму предсказанных значений с использованием метода `predict` настроенной модели.

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
