# オフセットを使ってPolyCollectionを作成する

```python
col = collections.PolyCollection(
    [spiral], offsets=xyo, offset_transform=ax2.transData)
trans = transforms.Affine2D().scale(fig.dpi/72.0)
col.set_transform(trans)
col.set_color(colors)

ax2.add_collection(col, autolim=True)
ax2.autoscale_view()

ax2.set_title('PolyCollection using offsets')
```

5番目のステップは、オフセットを使ってPolyCollectionを作成することです。曲線に色を塗りつぶすためにPolyCollectionを使用します。また、offset_transformを使って曲線の位置を設定します。
