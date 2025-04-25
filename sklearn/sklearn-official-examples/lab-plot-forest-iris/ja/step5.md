# 決定面のプロット

このステップでは、定義されたモデルの決定面をアイリスデータセット上にプロットします。

```python
plot_idx = 1

for pair in ([0, 1], [0, 2], [2, 3]):
    for model in models:
        # 2 つの対応する特徴量のみを取り出す
        X = iris.data[:, pair]
        y = iris.target

        # シャッフル
        idx = np.arange(X.shape[0])
        np.random.seed(RANDOM_SEED)
        np.random.shuffle(idx)
        X = X[idx]
        y = y[idx]

        # 標準化
        mean = X.mean(axis=0)
        std = X.std(axis=0)
        X = (X - mean) / std

        # 学習
        model.fit(X, y)

        scores = model.score(X, y)
        # 各列とコンソール用のタイトルを作成するために、str() を使って
        # 文字列の不要な部分を切り取る
        model_title = str(type(model)).split(".")[-1][:-2][: -len("Classifier")]

        model_details = model_title
        if hasattr(model, "estimators_"):
            model_details += " with {} estimators".format(len(model.estimators_))
        print(model_details + " with features", pair, "has a score of", scores)

        plt.subplot(3, 4, plot_idx)
        if plot_idx <= len(models):
            # 各列の上部にタイトルを追加する
            plt.title(model_title, fontsize=9)

        # 次に、微細なメッシュを入力として使って決定境界をプロットし、
        # 塗りつぶされた等高線プロットにする
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(
            np.arange(x_min, x_max, plot_step), np.arange(y_min, y_max, plot_step)
        )

        # 単一の DecisionTreeClassifier をプロットするか、
        # 分類器のアンサンブルの決定面をアルファブレンドする
        if isinstance(model, DecisionTreeClassifier):
            Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)
            cs = plt.contourf(xx, yy, Z, cmap=cmap)
        else:
            # 使用中の推定器の数に応じてアルファブレンドレベルを選択する
            # （AdaBoost は十分な適合が早く達成される場合、最大数より少ない推定器を使用できることに注意）
            estimator_alpha = 1.0 / len(model.estimators_)
            for tree in model.estimators_:
                Z = tree.predict(np.c_[xx.ravel(), yy.ravel()])
                Z = Z.reshape(xx.shape)
                cs = plt.contourf(xx, yy, Z, alpha=estimator_alpha, cmap=cmap)

        # アンサンブル分類のセットをプロットするためのより粗いグリッドを作成する
        # これらは決定面で見るものとどのように異なるかを示すためのものであり、
        # これらの点は規則的に配置されており、黒い輪郭線はない
        xx_coarser, yy_coarser = np.meshgrid(
            np.arange(x_min, x_max, plot_step_coarser),
            np.arange(y_min, y_max, plot_step_coarser),
        )
        Z_points_coarser = model.predict(
            np.c_[xx_coarser.ravel(), yy_coarser.ravel()]
        ).reshape(xx_coarser.shape)
        cs_points = plt.scatter(
            xx_coarser,
            yy_coarser,
            s=15,
            c=Z_points_coarser,
            cmap=cmap,
            edgecolors="none",
        )

        # 学習ポイントをプロットする、これらはまとまっており、黒い輪郭線がある
        plt.scatter(
            X[:, 0],
            X[:, 1],
            c=y,
            cmap=ListedColormap(["r", "y", "b"]),
            edgecolor="k",
            s=20,
        )
        plot_idx += 1  # 次のプロットに進む

plt.suptitle("Classifiers on feature subsets of the Iris dataset", fontsize=12)
plt.axis("tight")
plt.tight_layout(h_pad=0.2, w_pad=0.2, pad=2.5)
plt.show()
```
