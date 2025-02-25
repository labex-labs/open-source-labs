# カラーバーを追加する

`inset_axes` 関数を使って、インセット グラフにカラーバーを追加します。カラーバーの幅、高さ、位置、および境界ボックスを設定します。

```python
cax = inset_axes(axins,
                 width="5%",  # width = 10% of parent_bbox width
                 height="100%",  # height : 50%
                 loc='lower left',
                 bbox_to_anchor=(1.05, 0., 1, 1),
                 bbox_transform=axins.transAxes,
                 borderpad=0,
                 )
fig.colorbar(im, cax=cax)
```
