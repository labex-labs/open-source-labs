# 每个类别一个信息特征、一个聚类

我们创建一个每个类别有一个信息特征和一个聚类的数据集，并将其绘制出来。

```python
plt.subplot(321)
plt.title("One informative feature, one cluster per class", fontsize="small")
X1, Y1 = make_classification(n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1)
plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
```
