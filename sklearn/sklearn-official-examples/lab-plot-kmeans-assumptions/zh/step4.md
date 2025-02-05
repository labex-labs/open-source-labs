# 可能的解决方案

我们将讨论一些针对 k 均值聚类局限性的可能解决方案。在以下代码块中，我们展示了如何为第一个数据集找到正确的聚类数，以及如何通过增加随机初始化的次数来处理大小不均的聚类。

```python
y_pred = KMeans(n_clusters=3, **common_params).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=y_pred)
plt.title("最优聚类数")
plt.show()

y_pred = KMeans(n_clusters=3, n_init=10, random_state=random_state).fit_predict(
    X_filtered
)
plt.scatter(X_filtered[:, 0], X_filtered[:, 1], c=y_pred)
plt.title("大小不均的聚类 \n多次初始化")
plt.show()
```
