# 主成分分析 (PCA) の実行

データセットの次元数を削減するために主成分分析 (PCA) を実行します。データを最初の 3 つの主成分に射影し、結果を 3D でプロットします。

```python
fig = plt.figure(1, figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d", elev=-150, azim=110)

X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    X_reduced[:, 2],
    c=y,
    cmap=plt.cm.Set1,
    edgecolor="k",
    s=40,
)

ax.set_title("最初の 3 つの PCA 方向")
ax.set_xlabel("第 1 固有ベクトル")
ax.xaxis.set_ticklabels([])
ax.set_ylabel("第 2 固有ベクトル")
ax.yaxis.set_ticklabels([])
ax.set_zlabel("第 3 固有ベクトル")
ax.zaxis.set_ticklabels([])
```
