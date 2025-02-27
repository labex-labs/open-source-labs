# 結果を可視化する

このステップでは、特徴量の離散化プロセスの結果を可視化します。各分類器とデータセットに対するテストセット上の分類精度をプロットします。

```python
plt.tight_layout()

# グラフの上にサブタイトルを追加
plt.subplots_adjust(top=0.90)
suptitles = [
    "線形分類器",
    "特徴量の離散化と線形分類器",
    "非線形分類器",
]
for i, suptitle in zip([1, 3, 5], suptitles):
    ax = axes[0, i]
    ax.text(
        1.05,
        1.25,
        suptitle,
        transform=ax.transAxes,
        horizontalalignment="center",
        size="x-large",
    )
plt.show()
```
