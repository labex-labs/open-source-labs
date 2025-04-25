# 拟合回归模型

然后，我们使用 5 个近邻以及均匀权重和距离权重，将回归模型拟合到样本数据上。我们使用一个 for 循环来遍历每种权重类型，并使用拟合模型的`predict`方法创建数据点的散点图和预测值的线图。

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
