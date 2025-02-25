# Erstellen einer LineCollection mit Verschiebungen

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

Als vierter Schritt erstellen wir eine LineCollection mit Verschiebungen. Wir werden die LineCollection verwenden, um Kurven mit Verschiebungen zu erstellen. Wir werden auch die offset_transform verwenden, um die Positionen der Kurven festzulegen.
