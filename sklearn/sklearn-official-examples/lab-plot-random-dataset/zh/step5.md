# 每个类别两个信息特征、两个聚类

我们创建一个每个类别有两个信息特征和两个聚类的数据集，并将其绘制出来。

```python
plt.subplot(323)
plt.title("Two informative features, two clusters per class", fontsize="small")
X2, Y2 = make_classification(n_features=2, n_redundant=0, n_informative=2)
plt.scatter(X2[:, 0], X2[:, 1], marker="o", c=Y2, s=25, edgecolor="k")
```
