# 方向を示すためのテキスト矢印を追加する

データの方向を示すために、`ax.text()` 関数と `boxstyle` を "rarrow" に設定した `bbox` パラメータを使って、テキスト矢印を追加します。

```python
bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(0, 0, "Direction", ha="center", va="center", rotation=45,
            size=15,
            bbox=bbox_props)

bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.6)
```
