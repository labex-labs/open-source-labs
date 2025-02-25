# オフセットを使ってLineCollectionを作成する

```python
col = collections.LineCollection(
    [spiral], offsets=xyo, offset_transform=ax1.transData)
trans = fig.dpi_scale_trans + transforms.Affine2D().scale(1.0/72.0)
col.set_transform(trans)
col.set_color(colors)

ax1.add_collection(col, autolim=True)
ax1.autoscale_view()

ax1.set_title('LineCollection using offsets')
```

4番目のステップは、オフセットを使ってLineCollectionを作成することです。オフセット付きの曲線を作成するためにLineCollectionを使用します。また、offset_transformを使って曲線の位置を設定します。
