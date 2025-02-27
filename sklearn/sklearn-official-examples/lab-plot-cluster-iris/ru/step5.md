# Визуализация кластеров

После применения алгоритма K-Means Clustering давайте визуализируем образовавшиеся кластеры. Мы будем использовать трехмерный точечный график для визуализации точек данных и их соответствующих кластеров.

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=kmeans.labels_)
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
plt.show()
```
