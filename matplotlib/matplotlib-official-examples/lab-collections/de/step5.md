# Erstellen einer PolyCollection mit Verschiebungen

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

Als fünfter Schritt erstellen wir eine PolyCollection mit Verschiebungen. Wir werden die PolyCollection verwenden, um die Kurven mit Farben zu füllen. Wir werden auch die offset_transform verwenden, um die Positionen der Kurven festzulegen.
