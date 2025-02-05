# 在 PCA 降维后的数据上可视化结果

我们将使用主成分分析（PCA）将数据集降维到二维，并在这个新空间中绘制数据和聚类。

```python
import matplotlib.pyplot as plt

reduced_data = PCA(n_components=2).fit_transform(data)
kmeans = KMeans(init="k-means++", n_clusters=n_digits, n_init=4)
kmeans.fit(reduced_data)

# 网格的步长。减小步长可提高量化的质量。
h = 0.02  # 网格中的点 [x_min, x_max]x[y_min, y_max]。

# 绘制决策边界。为此，我们将为每个点分配一种颜色
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# 获取网格中每个点的标签。使用最后训练的模型。
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# 将结果放入彩色图中
Z = Z.reshape(xx.shape)
plt.figure(1)
plt.clf()
plt.imshow(
    Z,
    interpolation="nearest",
    extent=(xx.min(), xx.max(), yy.min(), yy.max()),
    cmap=plt.cm.Paired,
    aspect="auto",
    origin="lower",
)

plt.plot(reduced_data[:, 0], reduced_data[:, 1], "k.", markersize=2)
# 将质心绘制为白色 X
centroids = kmeans.cluster_centers_
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="x",
    s=169,
    linewidths=3,
    color="w",
    zorder=10,
)
plt.title(
    "K 均值聚类在数字数据集上（PCA 降维后的数据）\n"
    "质心用白色十字标记"
)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()
```
