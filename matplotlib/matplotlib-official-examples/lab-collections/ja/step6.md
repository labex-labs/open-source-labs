# オフセットを使ってRegularPolyCollectionを作成する

```python
col = collections.RegularPolyCollection(
    7, sizes=np.abs(xx) * 10.0, offsets=xyo, offset_transform=ax3.transData)
trans = transforms.Affine2D().scale(fig.dpi / 72.0)
col.set_transform(trans)
col.set_color(colors)

ax3.add_collection(col, autolim=True)
ax3.autoscale_view()

ax3.set_title('RegularPolyCollection using offsets')
```

6番目のステップは、オフセットを使ってRegularPolyCollectionを作成することです。オフセット付きの正多角形を作成するためにRegularPolyCollectionを使用します。また、offset_transformを使って多角形の位置を設定します。
