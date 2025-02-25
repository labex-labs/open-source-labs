# Erstellen einer RegularPolyCollection mit Verschiebungen

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

Als sechster Schritt erstellen wir eine RegularPolyCollection mit Verschiebungen. Wir werden die RegularPolyCollection verwenden, um regelmäßige Polygone mit Verschiebungen zu erstellen. Wir werden auch die offset_transform verwenden, um die Positionen der Polygone festzulegen.
