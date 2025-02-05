# 可视化数据

我们将使用散点图来可视化鸢尾花数据集。我们将绘制萼片长度与萼片宽度的关系，并根据点所属的类别为其着色。

```python
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5

plt.figure(2, figsize=(8, 6))
plt.clf()

# 绘制训练点
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor="k")
plt.xlabel("萼片长度")
plt.ylabel("萼片宽度")

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
```
