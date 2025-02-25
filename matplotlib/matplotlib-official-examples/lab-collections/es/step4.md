# Crear LineCollection utilizando desplazamientos

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

El cuarto paso es crear una LineCollection utilizando desplazamientos. Utilizaremos la LineCollection para crear curvas con desplazamientos. También utilizaremos el offset_transform para establecer las posiciones de las curvas.
