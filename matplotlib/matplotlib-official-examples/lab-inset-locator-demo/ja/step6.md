# 軸の外にインセットを作成する

`bbox_to_anchor` パラメータを使って軸の外に広がる軸座標でのバウンディングボックスを指定することで、軸の外にインセットを作成できます。

```python
# 軸の外にインセットを作成する
axins = inset_axes(ax, width="100%", height="100%",
                   bbox_to_anchor=(1.05,.6,.5,.4),
                   bbox_transform=ax.transAxes, loc=2, borderpad=0)
```
