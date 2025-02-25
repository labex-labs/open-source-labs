# テキストの境界ボックスを強調する

`rotation_mode` が `'default'` に設定されている場合、矩形を使ってテキストの境界ボックスを強調します。`get_window_extent` 関数を使って境界ボックスを取得し、`transData` 属性を使ってデータ座標に変換します。

```python
if mode == "default":
    fig.canvas.draw()
    for ax, text in texts.items():
        bb = text.get_window_extent().transformed(ax.transData.inverted())
        rect = plt.Rectangle((bb.x0, bb.y0), bb.width, bb.height,
                             facecolor="C1", alpha=0.3, zorder=2)
        ax.add_patch(rect)
```
