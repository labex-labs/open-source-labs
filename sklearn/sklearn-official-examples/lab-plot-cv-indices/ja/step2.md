# 交差検証インデックスを可視化する

このステップでは、各交差検証オブジェクトの挙動を可視化する関数を定義します。データを4分割します。各分割で、学習セット（青）とテストセット（赤）に選択されたインデックスを可視化します。

```python
def plot_cv_indices(cv, X, y, group, ax, n_splits, lw=10):
    """交差検証オブジェクトのインデックスのサンプルプロットを作成する。"""

    # 各CV分割に対する学習/テストの可視化を生成する
    for ii, (tr, tt) in enumerate(cv.split(X=X, y=y, groups=group)):
        # 学習/テストグループでインデックスを埋める
        indices = np.array([np.nan] * len(X))
        indices[tt] = 1
        indices[tr] = 0

        # 結果を可視化する
        ax.scatter(
            range(len(indices)),
            [ii + 0.5] * len(indices),
            c=indices,
            marker="_",
            lw=lw,
            cmap=cmap_cv,
            vmin=-0.2,
            vmax=1.2,
        )

    # 最後にデータのクラスとグループをプロットする
    ax.scatter(
        range(len(X)), [ii + 1.5] * len(X), c=y, marker="_", lw=lw, cmap=cmap_data
    )

    ax.scatter(
        range(len(X)), [ii + 2.5] * len(X), c=group, marker="_", lw=lw, cmap=cmap_data
    )

    # フォーマット設定
    yticklabels = list(range(n_splits)) + ["class", "group"]
    ax.set(
        yticks=np.arange(n_splits + 2) + 0.5,
        yticklabels=yticklabels,
        xlabel="Sample index",
        ylabel="CV iteration",
        ylim=[n_splits + 2.2, -0.2],
        xlim=[0, 100],
    )
    ax.set_title("{}".format(type(cv).__name__), fontsize=15)
    return ax
```
