# RBF 核支持向量机和线性支持向量机的决策面

```python
# 可视化决策面，投影到数据集的前两个主成分上
pca = PCA(n_components=8).fit(data_train)

X = pca.transform(data_train)

# 沿着前两个主成分生成网格
multiples = np.arange(-2, 2, 0.1)
# 沿着第一个成分的步长
first = multiples[:, np.newaxis] * pca.components_[0, :]
# 沿着第二个成分的步长
second = multiples[:, np.newaxis] * pca.components_[1, :]
# 合并
grid = first[np.newaxis, :, :] + second[:, np.newaxis, :]
flat_grid = grid.reshape(-1, data.shape[1])

# 绘图标题
titles = [
    "带 rbf 核的支持向量分类器",
    "带傅里叶 rbf 特征映射的支持向量分类器（线性核）\nn_components=100",
    "带 Nystroem rbf 特征映射的支持向量分类器（线性核）\nn_components=100",
]

plt.figure(figsize=(18, 7.5))
plt.rcParams.update({"font.size": 14})
# 预测并绘图
for i, clf in enumerate((kernel_svm, nystroem_approx_svm, fourier_approx_svm)):
    # 绘制决策边界。为此，我们将为网格 [x_min, x_max]x[y_min, y_max] 中的每个点分配一种颜色。
    plt.subplot(1, 3, i + 1)
    Z = clf.predict(flat_grid)

    # 将结果放入颜色图中
    Z = Z.reshape(grid.shape[:-1])
    levels = np.arange(10)
    lv_eps = 0.01  # 调整从计算出的等高线级别到颜色的映射。
    plt.contourf(
        multiples,
        multiples,
        Z,
        levels=levels - lv_eps,
        cmap=plt.cm.tab10,
        vmin=0,
        vmax=10,
        alpha=0.7,
    )
    plt.axis("off")

    # 也绘制训练点
    plt.scatter(
        X[:, 0],
        X[:, 1],
        c=targets_train,
        cmap=plt.cm.tab10,
        edgecolors=(0, 0, 0),
        vmin=0,
        vmax=10,
    )

    plt.title(titles[i])
plt.tight_layout()
plt.show()
```
