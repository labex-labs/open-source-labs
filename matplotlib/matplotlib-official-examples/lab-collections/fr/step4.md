# Créez une LineCollection à l'aide de décalages

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

La quatrième étape est de créer une LineCollection à l'aide de décalages. Nous utiliserons la LineCollection pour créer des courbes avec des décalages. Nous utiliserons également l'offset_transform pour définir les positions des courbes.
