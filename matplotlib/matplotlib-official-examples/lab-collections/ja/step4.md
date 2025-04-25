# オフセットを使って LineCollection を作成する

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

4 番目のステップは、オフセットを使って LineCollection を作成することです。オフセット付きの曲線を作成するために LineCollection を使用します。また、offset_transform を使って曲線の位置を設定します。
