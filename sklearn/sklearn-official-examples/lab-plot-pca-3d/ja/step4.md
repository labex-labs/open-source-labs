# PCA の結果を可視化する

主成分をプロットすることで、PCA の結果を可視化できます。データの 3D 散布図を作成し、各点をその密度に基づいて色分けします。その後、最初の 2 つの主成分を平面としてプロットします。このプロセスをデータの 2 つの異なるビューに対して繰り返します。

```python
fig = plt.figure(figsize=(10, 5))

# 最初のビュー
ax = fig.add_subplot(121, projection="3d", elev=-40, azim=-80)
ax.set_title("ビュー 1")

# データをプロットする
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# 主成分をプロットする
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

# 2 番目のビュー
ax = fig.add_subplot(122, projection="3d", elev=30, azim=20)
ax.set_title("ビュー 2")

# データをプロットする
density = np.exp(-(x ** 2 + y ** 2))
ax.scatter(x, y, z, c=density, cmap="plasma", marker="+", alpha=0.4)

# 主成分をプロットする
v1 = components[:, 0]
v2 = components[:, 1]
x_pca_plane = np.array([v1[0], -v1[0], -v1[0], v1[0]])
y_pca_plane = np.array([v1[1], -v1[1], -v1[1], v1[1]])
z_pca_plane = np.array([v1[2], -v1[2], v1[2], v1[2]])
ax.plot_surface(x_pca_plane, y_pca_plane, z_pca_plane, alpha=0.2)

plt.show()
```
