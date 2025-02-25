# Créez une RegularPolyCollection à l'aide de décalages

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

La sixième étape est de créer une RegularPolyCollection à l'aide de décalages. Nous utiliserons la RegularPolyCollection pour créer des polygones réguliers avec des décalages. Nous utiliserons également l'offset_transform pour définir les positions des polygones.
