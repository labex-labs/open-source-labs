# Crear PolyCollection utilizando desplazamientos

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

El quinto paso es crear una PolyCollection utilizando desplazamientos. Utilizaremos la PolyCollection para llenar las curvas con colores. También utilizaremos el offset_transform para establecer las posiciones de las curvas.
