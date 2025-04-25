# 可视化聚类

让我们可视化由 K 均值算法形成的聚类。

```python
# 获取每个数据点的聚类标签
labels = kmeans.labels_

# 用颜色编码的聚类绘制数据点
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()
```
