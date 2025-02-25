# 任意の位置にインセットを作成する

`bbox_to_anchor` パラメータを使ってデータ座標でのバウンディングボックスを指定し、`bbox_transform` パラメータを使ってバウンディングボックスの変換を指定することで、任意の位置にインセットを作成できます。

```python
# ax.transDataを変換として使用してデータ座標でインセットを作成する
axins3 = inset_axes(ax2, width="100%", height="100%",
                    bbox_to_anchor=(1e-2, 2, 1e3, 3),
                    bbox_transform=ax2.transData, loc=2, borderpad=0)
```
