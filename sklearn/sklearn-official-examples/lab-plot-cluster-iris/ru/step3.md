# Визуализация данных

Прежде чем применить алгоритм K-Means Clustering, давайте сначала визуализируем данные, чтобы лучше понять их. Мы будем использовать трехмерный точечный график для визуализации данных.

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
plt.show()
```
