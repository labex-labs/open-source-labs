# PCAにより次元削減したデータの結果を可視化する

PCAを使ってデータセットを2次元に削減し、この新しい空間でデータとクラスタをプロットします。

```python
import matplotlib.pyplot as plt

reduced_data = PCA(n_components=2).fit_transform(data)
kmeans = KMeans(init="k-means++", n_clusters=n_digits, n_init=4)
kmeans.fit(reduced_data)

# メッシュのステップサイズ。VQの品質を向上させるには、この値を小さくする。
h = 0.02  # メッシュ内の点 [x_min, x_max]x[y_min, y_max]。

# 決定境界をプロットする。そのために、各点に色を割り当てます。
x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# メッシュ内の各点に対するラベルを取得する。最後に学習したモデルを使用する。
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# 結果をカラープロットにする
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
# 重心を白いXでプロットする
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
    "K-meansクラスタリング on the digits dataset (PCAにより次元削減したデータ)\n"
    "重心は白い十字でマークされています"
)
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()
```
