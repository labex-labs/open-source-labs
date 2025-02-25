# Crear RegularPolyCollection utilizando desplazamientos

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

El sexto paso es crear una RegularPolyCollection utilizando desplazamientos. Utilizaremos la RegularPolyCollection para crear polígonos regulares con desplazamientos. También utilizaremos el offset_transform para establecer las posiciones de los polígonos.
