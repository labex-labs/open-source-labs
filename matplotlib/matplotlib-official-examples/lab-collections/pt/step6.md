# Criar RegularPolyCollection usando deslocamentos (offsets)

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

O sexto passo é criar um RegularPolyCollection usando deslocamentos (offsets). Usaremos o RegularPolyCollection para criar polígonos regulares com deslocamentos. Também usaremos o offset_transform para definir as posições dos polígonos.
