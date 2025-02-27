# RBFカーネルSVMと線形SVMの決定面

```python
# 決定面を可視化します。データセットの最初の2つの主成分に射影します
pca = PCA(n_components=8).fit(data_train)

X = pca.transform(data_train)

# 最初の2つの主成分に沿ってグリッドを生成します
multiples = np.arange(-2, 2, 0.1)
# 最初の成分に沿ったステップ
first = multiples[:, np.newaxis] * pca.components_[0, :]
# 2番目の成分に沿ったステップ
second = multiples[:, np.newaxis] * pca.components_[1, :]
# 結合
grid = first[np.newaxis, :, :] + second[:, np.newaxis, :]
flat_grid = grid.reshape(-1, data.shape[1])

# プロットのタイトル
titles = [
    "rbfカーネルを持つSVC",
    "Fourier rbf特徴マップを持つSVC(線形カーネル)\nn_components=100",
    "Nystroem rbf特徴マップを持つSVC(線形カーネル)\nn_components=100",
]

plt.figure(figsize=(18, 7.5))
plt.rcParams.update({"font.size": 14})
# 予測とプロット
for i, clf in enumerate((kernel_svm, nystroem_approx_svm, fourier_approx_svm)):
    # 決定境界をプロットします。そのために、メッシュ[x_min, x_max]x[y_min, y_max]内の各点に色を割り当てます。
    plt.subplot(1, 3, i + 1)
    Z = clf.predict(flat_grid)

    # 結果をカラープロットに入れます
    Z = Z.reshape(grid.shape[:-1])
    levels = np.arange(10)
    lv_eps = 0.01  # 計算された等高線レベルから色へのマッピングを調整します。
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

    # 訓練ポイントもプロットします
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
