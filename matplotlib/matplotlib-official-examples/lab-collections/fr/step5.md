# Créez une PolyCollection à l'aide de décalages

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

La cinquième étape est de créer une PolyCollection à l'aide de décalages. Nous utiliserons la PolyCollection pour remplir les courbes de couleurs. Nous utiliserons également l'offset_transform pour définir les positions des courbes.
