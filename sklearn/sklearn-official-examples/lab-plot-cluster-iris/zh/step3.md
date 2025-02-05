# 可视化数据

在应用K均值聚类算法之前，让我们先对数据进行可视化，以便更好地理解它。我们将使用三维散点图来可视化数据。

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2])
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
plt.show()
```
