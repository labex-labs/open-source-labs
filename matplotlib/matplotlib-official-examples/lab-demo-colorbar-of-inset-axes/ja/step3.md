# インセット グラフの作成

`zoomed_inset_axes` 関数を使ってインセット グラフを作成します。ズームレベルと、メイン プロット内のインセット グラフの位置を設定します。

```python
axins = zoomed_inset_axes(ax, zoom=2, loc='upper left')
axins.set(xticks=[], yticks=[])
```
