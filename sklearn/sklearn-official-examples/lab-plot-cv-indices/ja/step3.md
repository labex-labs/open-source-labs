# 交差検証オブジェクトを比較する

このステップでは、異なる scikit-learn の交差検証オブジェクトの交差検証の挙動を比較します。いくつかの一般的な交差検証オブジェクトをループ処理し、それぞれの挙動を可視化します。どのようにいくつかはグループ/クラス情報を使用し、他のものは使用しないかをご注目ください。

```python
cvs = [
    KFold,
    GroupKFold,
    ShuffleSplit,
    StratifiedKFold,
    StratifiedGroupKFold,
    GroupShuffleSplit,
    StratifiedShuffleSplit,
    TimeSeriesSplit,
]

for cv in cvs:
    this_cv = cv(n_splits=n_splits)
    fig, ax = plt.subplots(figsize=(6, 3))
    plot_cv_indices(this_cv, X, y, groups, ax, n_splits)

    ax.legend(
        [Patch(color=cmap_cv(0.8)), Patch(color=cmap_cv(0.02))],
        ["Testing set", "Training set"],
        loc=(1.02, 0.8),
    )
    # 凡例を収まるようにする
    plt.tight_layout()
    fig.subplots_adjust(right=0.7)
plt.show()
```
