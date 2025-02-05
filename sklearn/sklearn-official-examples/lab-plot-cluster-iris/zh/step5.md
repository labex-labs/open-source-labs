# 可视化聚类结果

在应用K均值聚类算法之后，让我们来可视化形成的聚类。我们将使用三维散点图来可视化数据点及其各自所属的聚类。

```python
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=kmeans.labels_)
ax.set_xlabel("Sepal length")
ax.set_ylabel("Sepal width")
ax.set_zlabel("Petal length")
plt.show()
```
